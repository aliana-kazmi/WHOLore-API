from django.test import SimpleTestCase
from django.urls import reverse, resolve
from characters.views import *


class TestUrls(SimpleTestCase):

    def test_all_companions_url_is_resolved(self):
        url = reverse('all-companions')
        print(resolve(url))
        self.assertEquals(resolve(url).func, CompanionView)

    def test_all_alien_races_url_is_resolved(self):
        url = reverse('all-alien-races')
        print(resolve(url))
        self.assertEquals(resolve(url).func, AlienView)

    def test_all_villains_url_is_resolved(self):
        url = reverse('all-villains')
        print(resolve(url))
        self.assertEquals(resolve(url).func, VillainView)

    def test_all_doctors_url_is_resolved(self):
        url = reverse('all-doctors')
        print(resolve(url))
        self.assertEquals(resolve(url).func, DoctorView)