from  django.shortcuts import render_to_response
from django.http import Http404
import simplejson as json
from django.http import HttpResponseRedirect
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

    return render_to_response('course/show.html', {'courses': courses}) 


def show(request, department, number, status=''):
    """ shows information about single course and can register from here """
    regclass = request.session['regclass']

    regerror = 0
    if status == "error":
        regerror = 1

    # to come back when redirecting to a different view func
    request.session['prevcourse'] = department+number

    courses = regclass.class_search(department, number)
    if courses is None:
        raise Http404 

    if request.method == 'GET': 
        return render_to_response('course/show.html', {'courses':courses, 'regerror': regerror}) 

    # user sumbitted crns to register for courses, use urls to redirect to register view
    crn_list_reg = request.POST.getlist('choose')
    if len(crn_list_reg) is 1: 
        return HttpResponseRedirect('/course/register/' + crn_list_reg[0])
    else:
        return HttpResponseRedirect('/course/register/' + crn_list_reg[0] + "&" + crn_list_reg[1])


def register(request, crn1, crn2=""):    
    """ register via parsing the url and calling the add_class """ 
    regclass = request.session['regclass']

    error = regclass.add_class(crn1, crn2)
    
    if error:
        return HttpResponseRedirect('/course/' + request.session['prevcourse'] + '?status=error')
    return HttpResponseRedirect('/course/' + request.session['prevcourse'] + '?status=success')
  
