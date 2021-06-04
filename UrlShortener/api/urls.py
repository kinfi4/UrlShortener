from django.urls import path

from api.views import UrlAPIUrlShortener, UrlAPIRedirectView

urlpatterns = [
    path('<str:url>', UrlAPIRedirectView.as_view(), name='api_redirect'),
    path('', UrlAPIUrlShortener.as_view(), name='api_shortener'),
]
