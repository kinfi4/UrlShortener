from django.http import HttpRequest, Http404, HttpResponseBadRequest, JsonResponse
from django.views import View

from api.handlers import get_real_url, add_new_or_get_existing_url
from api.exception import UnknownUrlError


class UrlAPIRedirectView(View):
    def get(self, request: HttpRequest, url):
        try:
            real_url = get_real_url(url)
        except UnknownUrlError:
            raise Http404

        return JsonResponse(data={'real_url': real_url})


class UrlAPIUrlShortener(View):
    def post(self, request: HttpRequest):
        real_url = request.POST.get('real_url')

        if not real_url:
            return HttpResponseBadRequest(content_type='application/json',
                                          content={'error': 'You did not specified the url'})

        url, created = add_new_or_get_existing_url(real_url)

        if created:
            return JsonResponse(status=201, data={'short_url': url.short_url})
        else:
            return JsonResponse(status=200, data={'short_url': url.short_url})
