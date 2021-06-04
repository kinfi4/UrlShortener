from django.http import JsonResponse, HttpRequest, Http404, HttpResponsePermanentRedirect
from django.views import View


class UrlAPIView(View):
    def get(self, request: HttpRequest):
        pass

    def post(self, request: HttpRequest):
        pass
