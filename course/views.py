from  django.shortcuts import render_to_response
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.template import RequestContext, Template
import simplejson as json
import reglib

def index(request):
    """ main course page that contains a search bar """

    if not 'regclass' in request.session:
        return HttpResponseRedirect('/')
    regclass = request.session['regclass']

    if request.method == 'GET':
        return render_to_response('course/index.html')

    # Search form for jumping to a course info page (show)
    course = request.POST['course']
    course = reglib.utilities.utilities.format_course(course)
    course_dict = reglib.utilities.utilities.course_to_dep_and_num(course)
    try:
        department = course_dict['department']
        number = course_dict['number']
        courses = regclass.class_search(course_dict['department'], course_dict['number'])
    except:
        return render_to_response('course/index.html', {'course_not_found':course})

    return HttpResponseRedirect('/course/' + department + number + '/') 


def show(request, department, number, status=''):
    """ shows information about single course and can register from here """
    course = department + number
    regclass = request.session['regclass']

    courses = regclass.class_search(department, number)
    if courses is None:
        raise Http404 

    if request.method == 'GET': 
        find_time_conflicts(regclass, courses)
        return render_to_response('course/show.html', {'courses':courses})

    # user sumbitted crns to register for courses, use urls to redirect to register view
    crn_list_reg = request.POST.getlist('choose')
    if len(crn_list_reg) is 1: 
        success = register(request, course, crn_list_reg[0])
    else:
        success = register(request, course, crn_list_reg[0], crn_list_reg[1])

    # display confirmation or error message if register success/fail
    if not success:
        messages.error(request, "Failed to register for " + course ) 
    else:
        messages.success(request, "Successfully registered for " + course) 

    return render_to_response('course/show.html', {'courses':courses}, context_instance=RequestContext(request))


def register(request, course, crn1, crn2=""):    
    """ register for course """ 

    regclass = request.session['regclass']
    return regclass.add_class(crn1, crn2)


def find_time_conflicts(regclass, courses):
    """ given a list of courses, checks current and next schedule for time conflicts """
    schedules = [regclass.schedule, regclass.next_schedule]
    for schedule in schedules:
        for course in courses:
            course['conflict'] = None 
            term = reglib.utilities.utilities.adjust_schedule_term(schedule.current_term)
            term = reglib.utilities.utilities.format_term(term)
            if course['term'] != term: 
                continue
            else:
                for course_sched in schedule.current_classes:
                    if reglib.utilities.class_search_conflict(course, course_sched):
                        course['conflict'] = course_sched['department'] + course_sched['number']
                    
        
  
