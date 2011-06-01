from  django.shortcuts import render_to_response
from django.http import Http404
import simplejson as json
from django.http import HttpResponseRedirect
import reglib

def index(request):
    if 'regclass' in request.session:
        
        return HttpResponseRedirect('/main')
    return render_to_response('index.html', {'no_show_nav': 1})

def login(request):
    if 'regclass' in request.session:
        return HttpResponseRedirect('/main')
    if request.method == 'GET':
        return render_to_response('index.html')
    
    username = request.POST['username']
    password = request.POST['password']

    try:
        regclass = reglib.infosu(username, password)
        request.session['regclass'] = regclass
        request.session.set_expiry(1200)
        return HttpResponseRedirect('/main')
    except:
        return HttpResponseRedirect('/')

def logout(request):
    del(request.session['regclass'])
    return HttpResponseRedirect('/')

def main(request):
    if not 'regclass' in request.session:
        return HttpResponseRedirect('/')
    regclass = request.session['regclass']
    return render_to_response('main.html')

def scheduler(request):
    if not 'regclass' in request.session:
        return HttpResponseRedirect('/')

    if request.method == 'GET':
        return render_to_response('scheduler/index.html')
    regclass = request.session['regclass']
    try:
        classes = request.POST['classes'].split(', ')
        term_year = request.POST['term'] + request.POST['year']
        combinations = regclass.make_schedule(classes, term_year)
        combinations_json = json.dumps(combinations)
    except:
        return render_to_response('scheduler/index.html')

    return render_to_response('scheduler/index.html', {'combinations':combinations, 'json':combinations_json, 'range':range(24)})

def show_course(request, department, course_number):
    regclass = request.session['regclass']

    courses = regclass.class_search(department, course_number)
    if courses is None:
        raise Http404 
    
    return render_to_response('courses/show.html', {'courses': courses, 'department': department, 'course_number': course_number})
    
