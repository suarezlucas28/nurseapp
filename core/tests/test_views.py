from django.test import TestCase, Client
from django.urls import resolve, reverse


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.history_url = reverse('history')

    def test_history_new_query(self):
        response = self.client.post(self.history_url, {'idNumber': '7628133', 'age': '29', 'catcha': 'AAAA'})
        self.assertEqual(
            response.status_code, 200
        )
