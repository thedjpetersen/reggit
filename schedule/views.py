from  django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.template import RequestContext, Template
import simplejson as json
from reglib.utilities import utilities

# Create your views here.

def index(request):
    """ gets current term's schedule and handles dropping of courses """

    regclass = request.session['regclass']
    # to print term to screen
    term = utilities.adjust_schedule_term(regclass.schedule.current_term)
    term = utilities.format_term(term, True)

    # if user post a form to drop classes
    if request.method == 'POST':
        crn_list_drop = request.POST.getlist('drop')
        success = regclass.drop_classes(crn_list_drop)
        if success:
            messages.success(request, "Successfully dropped course(s)")
        else:
            messages.error(request, "There was an error dropping course(s)")
        regclass.get_current_schedule() # refresh

    # get schedule
    schedule = regclass.schedule.current_classes
    schedule_json = json.dumps(schedule)

    no_courses = False
    if len(schedule) is 0:
        no_courses = True

    if no_courses:
        return render_to_response('schedule/no_course.html', {'current_term': True, 'term': term})
    return render_to_response('schedule/index.html', {'schedule':schedule, 'term':term, 'range':range(24), 'json':schedule_json, 'current_term': True}, context_instance=RequestContext(request))


def next_term(request):
    """ gets next term's schedule and handles dropping of courses """

    regclass = request.session['regclass']
    # to print term to screen
    term = utilities.adjust_schedule_term(regclass.next_schedule.current_term)
    term = utilities.format_term(term, True)

    # if user post a form to drop classes
    if request.method == 'POST':
        crn_list_drop = request.POST.getlist('drop')
        success = regclass.drop_classes(crn_list_drop, True)
        if success:
            messages.success(request, "Successfully dropped course(s)")
        else:
            messages.error(request, "There was an error dropping course(s)")
        regclass.get_next_schedule() # refresh

    schedule = regclass.next_schedule.current_classes
    schedule_json = json.dumps(schedule)

    no_courses = False
    if len(schedule) is 0: 
        no_courses = True
    
    if no_courses:
        return render_to_response('schedule/no_course.html', {'current_term': False})
    return render_to_response('schedule/index.html', {'schedule':schedule, 'term':term, 'range':range(24), 'json':schedule_json, 'current_term': False}, context_instance=RequestContext(request))



