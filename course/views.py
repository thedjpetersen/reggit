from  django.shortcuts import render_to_response
from django.http import Http404
import simplejson as json
from django.http import HttpResponseRedirect
import reglib

def index(request):

    regclass = request.session['regclass']

    return render_to_response('course/index.html', {})

def show(request, department, course_number):
    regclass = request.session['regclass']

    courses = regclass.class_search(department, course_number)
    if courses is None:
        raise Http404 
    
    return render_to_response('course/show.html', {'courses': courses, 'department': department, 'course_number': course_number})
    
