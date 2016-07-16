from selenium import webdriver

from functional_tests.base import FunctionalTest
from team.models import Member


class TeamPageTest(FunctionalTest):
    def setUp(self):
        self.driver = webdriver.Chrome()
        Member.objects.create(
            name='M',
            position='Developer',
            information='I love mathematics and computer science.'
        )
        self.driver.get(self.live_server_url + '/team/')

    def tearDown(self):
        self.driver.quit()
        Member.objects.all().delete()

    def test_team_page_elements_are_displayed(self):
        members = Member.objects.all()
        displayed_members = self.driver.find_elements_by_class_name('member')

        self.assertEqual(len(members), len(displayed_members))

        for index in range(len(members)):
            member_name = displayed_members[index].find_element_by_tag_name('h2').text
            member_position = displayed_members[index].find_element_by_tag_name('h3').text
            member_information = displayed_members[index].find_element_by_tag_name('p').text
            self.assertEqual(members[index].name, member_name)
            self.assertEqual(members[index].position, member_position)
            self.assertEqual(members[index].information, member_information)
