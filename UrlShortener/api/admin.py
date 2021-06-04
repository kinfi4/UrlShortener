from django.contrib import admin

from api.models import Url


@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    ordering = ('-pub_date',)
