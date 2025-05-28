from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page

class HomePageTest(TestCase):
    def test_home_page_returns_correct_html(self):
        res = self.client.get('/')
        self.assertContains(res, '<html>')
        self.assertContains(res, '<title>To-Do lists</title>')
        self.assertContains(res, '</html>')


