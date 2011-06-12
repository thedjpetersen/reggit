from  django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
import reglib


# Create your views here.

def index(request):
    if not 'regclass' in request.session:
        return HttpResponseRedirect('/')

    regclass = request.session['regclass']
    transcript = regclass.transcript.sort_by_term()
    return render_to_response('transcript/index.html', {'transcript':transcript, 'credits': regclass.transcript.credits, 'gpa': regclass.transcript.gpa})


