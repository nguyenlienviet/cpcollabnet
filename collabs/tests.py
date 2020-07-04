from django.test import TestCase
from django.urls import reverse, resolve
from .views import home, researcher, search
from .models import *
from django.contrib.auth.models import User

class HomeTests(TestCase):
    def test_home_view_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

class ResearcherTests(TestCase):
    def setUp(self):
        url = reverse('researcher', kwargs={'rid':16})
        self.response = self.client.get(url)

    def test_researcher_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_board_topics_view_not_found_status_code(self):
        url = reverse('researcher', kwargs={'rid': -1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_researcher_url_resolves_home_view(self):
        view = resolve('/researchers/16')
        self.assertEquals(view.func, home)
