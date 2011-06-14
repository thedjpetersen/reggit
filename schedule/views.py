from  django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
import simplejson as json


# Create your views here.

def index(request):
    if not 'regclass' in request.session:
        return HttpResponseRedirect('/')

    regclass = request.session['regclass']
    schedule = regclass.schedule.current_classes
    schedule_json = json.dumps(schedule)

    no_courses = False
    if len(schedule) is 0:
        no_courses = True

    if no_courses:
        return render_to_response('schedule/no_course.html', {'current_term': True})
    return render_to_response('schedule/index.html', {'schedule':schedule, 'range':range(24), 'json':schedule_json, 'current_term': True})

def next_term(request):
    if not 'regclass' in request.session:
        return HttpResponseRedirect('/')

    regclass = request.session['regclass']
    schedule = regclass.next_schedule.current_classes
    schedule_json = json.dumps(schedule)

    no_courses = False
    if len(schedule) is 0: 
        no_courses = True
    
    if no_courses:
        return render_to_response('schedule/no_course.html', {'current_term': False})
    return render_to_response('schedule/index.html', {'schedule':schedule, 'range':range(24), 'json':schedule_json, 'current_term': False})



