from  django.shortcuts import render_to_response
from django.http import Http404
import simplejson as json
from django.http import HttpResponseRedirect
import reglib

def index(request):
    if not 'regclass' in request.session:
        return HttpResponseRedirect('/')

    if request.method == 'GET':
        return render_to_response('scheduler/index.html')

    # if user chose to register a list of courses
    try:
        if request.session['courses']:
            register(courses)
            del(request.session['courses'])
            return render_to_response('scheduler/index.html')
    except:
        pass
        
    regclass = request.session['regclass']
    #try:
    classes = request.POST['classes'].split(', ')
    term_year = request.POST['term'] + request.POST['year']
    results = regclass.make_schedule(classes, term_year)
    combinations = results['combinations']
    classes_possible = results['classes_possible']
    combinations_json = json.dumps(combinations)
    #except:
        #return render_to_response('scheduler/index.html')

    return render_to_response('scheduler/index.html', {'combinations':combinations, 'json':combinations_json, 'range':range(24), 'classes_possible':classes_possible})

def register(courses):
    print courses


