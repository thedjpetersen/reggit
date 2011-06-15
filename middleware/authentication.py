from django.http import HttpResponseRedirect

class AuthenticationMiddleware(object):

    def process_request(self, request):
        if len(request.path_info)>1:
            if 'regclass' not in request.session:
                return HttpResponseRedirect('/')
        return None
