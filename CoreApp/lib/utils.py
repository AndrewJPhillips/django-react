
from django.http import HttpResponseRedirect

class LoginMiddleware(object):

    def __init__(self, get_response):
            self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def is_auth(self, request):

        if not request.user or not request.user.is_authenticated():
            return HTTPResponseRedirect("/login/")

        return None