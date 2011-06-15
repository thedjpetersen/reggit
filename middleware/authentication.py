from django.http import HttpResponseRedirect

class AuthenticationMiddleware(object):

    def process_request(self, request):
        if not request.path_info[:12] == '/site_media/' and not request.path_info in [u'/', u'/login/']:
            if 'regclass' not in request.session:
                return HttpResponseRedirect('/')
        return None
