from  django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
import registration
# Create your views here.


def index(request):
    if not request.session['rc'] == None:
        return HttpResponseRedirect('/main')
    return render_to_response('index.html')

def login(request):
    if not request.session['rc'] == None:
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
    request.session['rc'] = None
    return HttpResponseRedirect('/')

def main(request):
    rc = request.session['rc']
    return render_to_response('main.html', {'rc':rc})

