from django.http import HttpRequest, Http404, HttpResponsePermanentRedirect, HttpResponseBadRequest, JsonResponse
from django.views import View

from api.handlers import get_real_url, add_new_url
from api.exception import UnknownUrlError, CantRewriteExistingUrlError


class UrlAPIRedirectView(View):
    def get(self, request: HttpRequest, url):
        try:
            real_url = get_real_url(url)
        except UnknownUrlError:
            raise Http404

        return HttpResponsePermanentRedirect(real_url)


class UrlAPIUrlShortener(View):
    def post(self, request: HttpRequest):
        real_url = request.POST.get('real_url')

        if not real_url:
            return HttpResponseBadRequest(content_type='application/json',
                                          content={'error': 'You did not specified the url'})

        try:
            url = add_new_url(real_url)
        except CantRewriteExistingUrlError:
            return HttpResponseBadRequest(content_type='application/json',
                                          content={'error': 'Short path for this url already exists'})

        return JsonResponse(status=201, data={'short_url': url})
