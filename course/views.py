from  django.shortcuts import render_to_response
from django.http import Http404
import simplejson as json
from django.http import HttpResponseRedirect
import reglib

def index(request):

    if not 'regclass' in request.session:
        return HttpResponseRedirect('/')
    regclass = request.session['regclass']

    if request.method == 'GET':
        return render_to_response('course/index.html')

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


def show(request, department, number):
    regclass = request.session['regclass']

    courses = regclass.class_search(department, number)
    if courses is None:
        raise Http404 
    
    return render_to_response('course/show.html', {'courses': courses})
    
