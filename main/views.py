from  django.shortcuts import render_to_response
import simplejson as json
from django.http import HttpResponseRedirect
import registration
# Create your views here.


def index(request):
    if 'rc' in request.session:
        return HttpResponseRedirect('/main')
    return render_to_response('index.html')

def login(request):
    if 'rc' in request.session:
        return HttpResponseRedirect('/main')
    if request.method == 'GET':
        return render_to_response('index.html')
    
    username = request.POST['username']
    password = request.POST['password']

    try:
        rc_class = registration.infosu(username, password)
        request.session['rc'] = rc_class
        return HttpResponseRedirect('/main')
    except:
        return HttpResponseRedirect('/')

def logout(request):
    if 'rc' in request.session:
        del(request.session['rc'])
    return HttpResponseRedirect('/')

def main(request):
    if not 'rc' in request.session:
        return HttpResponseRedirect('/')
    rc = request.session['rc']
    return render_to_response('main.html', {'rc':rc})


def transcript(request):
    if not 'rc' in request.session:
        return HttpResponseRedirect('/')

    rc = request.session['rc']
    transcript = rc.transcript.grades
    return render_to_response('transcript/index.html', {'transcript':transcript})

def schedule(request):
    if not 'rc' in request.session:
        return HttpResponseRedirect('/')

    rc = request.session['rc']
    schedule = rc.schedule.current_classes
    return render_to_response('schedule/index.html', {'schedule':schedule})


def make_schedule(request):
    if not 'rc' in request.session:
        return HttpResponseRedirect('/')

    if request.method == 'GET':
        return render_to_response('make_schedule.html')
    rc = request.session['rc']
    try:
        classes = request.POST['classes'].split(', ')
    except:
        return render_to_response('make_schedule.html')
    combinations = rc.make_schedule(classes)
    combinations_json = json.dumps(combinations)

    return render_to_response('make_schedule.html', {'combinations':combinations, 'json':combinations_json, 'range':range(24)})

