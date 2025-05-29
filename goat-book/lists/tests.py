from django.test import TestCase

class HomePageTest(TestCase):
    def test_home_page_returns_correct_html(self):
        res = self.client.get('/')
        self.assertTemplateUsed(res, 'home.html')

    def test_renders_home_page_content(self):
        res = self.client.get('/')
        self.assertContains(res, 'To-Do')

