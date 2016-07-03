from django.shortcuts import render

from team.models import Member


def team_page(request):
    members = Member.objects.all()
    return render(request, 'team/team.html', {
        'members': members,
    })
