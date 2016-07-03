from django.shortcuts import render


def team_page(request):
    return render(request, 'team/team.html')
