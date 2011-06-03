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

    return render_to_response('schedule/index.html', {'schedule':schedule, 'range':range(24), 'json':schedule_json})


