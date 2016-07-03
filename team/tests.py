from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase

from team.views import team_page


class TeamPageTest(TestCase):
    def test_team_page_uses_team_template(self):
        request = HttpRequest()
        response = team_page(request)
        expected_content = render_to_string('team/team.html')

        self.assertEqual(
            expected_content,
            response.content.decode()
        )
