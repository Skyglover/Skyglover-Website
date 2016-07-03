from django.contrib import admin

from home.models import SomeText


class SomeTextAdmin(admin.ModelAdmin):
    list_display = ('identifier', 'text')


admin.site.register(SomeText, SomeTextAdmin)
