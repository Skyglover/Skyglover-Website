from django.test import LiveServerTestCase
from selenium import webdriver

from helper.helper import verify_page_h1_is_displayed
from team.models import Member


class TeamPageTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        Member.objects.create(
            name='M',
            position='Developer',
            information='I love mathematics and computer science.'
        )
        self.browser.get(self.live_server_url + '/team/')

    def tearDown(self):
        self.browser.quit()
        Member.objects.all().delete()

    def test_team_page_elements_are_displayed(self):
        verify_page_h1_is_displayed(self, self.browser, 'Team')
        members = Member.objects.all()
        displayed_members = self.browser.find_elements_by_class_name('member')

        self.assertEqual(len(members), len(displayed_members))

        for index in range(len(members)):
            member_name = displayed_members[index].find_element_by_tag_name('h2').text
            member_position = displayed_members[index].find_element_by_tag_name('h3').text
            member_information = displayed_members[index].find_element_by_tag_name('p').text
            self.assertEqual(members[index].name, member_name)
            self.assertEqual(members[index].position, member_position)
            self.assertEqual(members[index].information, member_information)
