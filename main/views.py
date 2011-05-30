from  django.shortcuts import render_to_response
import simplejson as json
from django.http import HttpResponseRedirect
import reglib
# Create your views here.

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

def transcript(request):
    if not 'regclass' in request.session:
        return HttpResponseRedirect('/')

    regclass = request.session['regclass']
    transcript = regclass.transcript.sort_by_term()
    return render_to_response('transcript/index.html', {'transcript':transcript, 'credits': regclass.transcript.credits, 'gpa': regclass.transcript.gpa})

def schedule(request):
    if not 'regclass' in request.session:
        return HttpResponseRedirect('/')

    regclass = request.session['regclass']
    schedule = regclass.schedule.current_classes
    return render_to_response('schedule/index.html', {'schedule':schedule})

def make_schedule(request):
    if not 'regclass' in request.session:
        return HttpResponseRedirect('/')

    if request.method == 'GET':
        return render_to_response('make_schedule.html')
    regclass = request.session['regclass']
    try:
        classes = request.POST['classes'].split(', ')
    except:
        return render_to_response('make_schedule.html')
    combinations = regclass.make_schedule(classes)
    combinations_json = json.dumps(combinations)

    return render_to_response('make_schedule.html', {'combinations':combinations, 'json':combinations_json, 'range':range(24)})

