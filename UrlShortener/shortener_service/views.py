import requests
from django.shortcuts import render
from django.http import HttpRequest, HttpResponsePermanentRedirect
from django.views import View
from django.urls import reverse, NoReverseMatch
from django.conf import settings
from django.contrib import messages

from shortener_service.form import CutUrlForm, TranslateUrlForm


class TranslateUrlView(View):
    def get(self, request: HttpRequest):
        form = TranslateUrlForm()
        return render(request, 'translate_url.html', {'form': form})

    def post(self, request: HttpRequest):
        form = TranslateUrlForm(request.POST)

        if form.is_valid():
            try:
                url = settings.SITE_URL[:len(settings.SITE_URL) - 1] \
                      + reverse('api_redirect', args=(form.cleaned_data['short_url'],))
                result = requests.get(url)
            except NoReverseMatch:
                messages.error(request, 'You entered invalid token', extra_tags='alert alert-error')
                return render(request, 'translate_url.html', {'form': form})

            if result.status_code == 200:
                real_url = result.json()['real_url']
                return HttpResponsePermanentRedirect(real_url)

            messages.error(request, 'There is no url connected with this token', extra_tags='alert alert-error')
            return render(request, 'translate_url.html', {'form': form})

        return render(request, 'translate_url.html', {'form': form})


class CutUrlView(View):
    def get(self, request: HttpRequest):
        form = CutUrlForm()
        return render(request, 'shortener.html', {'form': form})

    def post(self, request: HttpRequest):
        form = CutUrlForm(request.POST)

        if form.is_valid():
            url = settings.SITE_URL[:len(settings.SITE_URL) - 1] + reverse('api_shortener')
            result = requests.post(url, data={'real_url': form.cleaned_data['full_url']})

            short_url = result.json()['short_url']

            form = TranslateUrlForm()
            form.fields['short_url'].initial = short_url

            messages.success(request, 'Token for link created', extra_tags='alert alert-success')
            return render(request, 'translate_url.html', {'form': form})
