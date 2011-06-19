from  django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
import simplejson as json
from reglib.utilities import utilities

# Create your views here.

def index(request):
    regclass = request.session['regclass']
    schedule = regclass.schedule.current_classes
    term = utilities.adjust_schedule_term(regclass.schedule.current_term)
    term = utilities.format_term(term, True)
    schedule_json = json.dumps(schedule)

    no_courses = False
    if len(schedule) is 0:
        no_courses = True

    if no_courses:
        return render_to_response('schedule/no_course.html', {'current_term': True, 'term': term})
    return render_to_response('schedule/index.html', {'schedule':schedule, 'term':term, 'range':range(24), 'json':schedule_json, 'current_term': True})

def next_term(request):
    regclass = request.session['regclass']
    schedule = regclass.next_schedule.current_classes
    term = utilities.adjust_schedule_term(regclass.next_schedule.current_term)
    term = utilities.format_term(term, True)
    schedule_json = json.dumps(schedule)

    no_courses = False
    if len(schedule) is 0: 
        no_courses = True
    
    if no_courses:
        return render_to_response('schedule/no_course.html', {'current_term': False})
    return render_to_response('schedule/index.html', {'schedule':schedule, 'term':term, 'range':range(24), 'json':schedule_json, 'current_term': False})



