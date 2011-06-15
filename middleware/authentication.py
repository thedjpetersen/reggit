from django.http import HttpResponseRedirect

class AuthenticationMiddleware(object):

    def process_request(self, request):
        if not request.path_info in ['/', '/login/']:
            if 'regclass' not in request.session:
                return HttpResponseRedirect('/')
        return None
