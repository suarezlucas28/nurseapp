from django.test import SimpleTestCase
from django.urls import resolve, reverse

from core.views import history_vital_sings


class TestUrls(SimpleTestCase):

    def test_history_url_is_resolve(
            self):
        url = reverse('history')
        self.assertEquals(
            resolve(url).func, history_vital_sings
        )
