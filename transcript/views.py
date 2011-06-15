from  django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
import reglib


# Create your views here.

def index(request):
    regclass = request.session['regclass']
    transcript = regclass.transcript.grades
    return render_to_response('transcript/index.html', {'transcript':transcript, 'credits': regclass.transcript.credits, 'gpa': regclass.transcript.gpa})

def report_card(request):
    regclass = request.session['regclass']
    transcript = regclass.transcript.sort_by_term()
    grade_distribution = tr.grade_distribution()
    term_groups = transcript.group_by_term()
    return render_to_response('transcript/report_card.html' ,{'grade_distribution':grade_distribution, 'term_groups':term_groups})
