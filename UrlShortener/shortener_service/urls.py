from django.urls import path

from shortener_service.views import TranslateUrlView, CutUrlView

urlpatterns = [
    path('translate', TranslateUrlView.as_view(), name='translate_url'),
    path('cut-url', CutUrlView.as_view(), name='cut_url')
]
