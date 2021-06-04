import requests
from django.shortcuts import render
from django.http import HttpRequest, HttpResponsePermanentRedirect
from django.views import View
from django.urls import reverse

from shortener_service.form import CutUrlForm, TranslateUrlForm


class TranslateUrlView(View):
    def get(self, request: HttpRequest):
        form = TranslateUrlForm()
        return render(request, 'translate_url.html', {'form': form})

    def post(self, request: HttpRequest):
        form = TranslateUrlForm(request.POST)

        if form.is_valid():
            result = requests.get(reverse('api_redirect'), params=(form.changed_data['short_url'],))

            if result.is_permanent_redirect:
                return HttpResponsePermanentRedirect(result.url)

            # TODO: Write messages

            return render(request, 'translate_url.html', {'form': form})

        return render(request, 'translate_url.html', {'form': form})


class CutUrlView(View):
    def get(self, request: HttpRequest):
        form = CutUrlForm()
        return render(request, 'shortener.html', {'form': form})

    def post(self, request: HttpRequest):
        pass
