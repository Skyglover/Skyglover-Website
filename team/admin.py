from django.contrib import admin

from team.models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')

admin.site.register(Member, MemberAdmin)
