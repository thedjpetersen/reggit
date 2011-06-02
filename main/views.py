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
        results = regclass.make_schedule(classes, term_year)
        combinations = results['combinations']
        classes_possible = results['classes_possible']
        combinations_json = json.dumps(combinations)
    except:
        return render_to_response('scheduler/index.html')

    return render_to_response('scheduler/index.html', {'combinations':combinations, 'json':combinations_json, 'range':range(24), 'classes_possible':classes_possible})

