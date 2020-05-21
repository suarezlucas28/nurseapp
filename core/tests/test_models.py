from django.test import TestCase

from core.models import Patient


class TestModels(TestCase):

	def setUp(self):
		self.patient1 = Patient.objects.create(
			firstName="Carlos",
			lastName="Salas",
			idNumber=5323553,
			age=22
		)

	def test_patient_is_saved(self):
		self.assertTrue(
			Patient.objects.filter(pk=self.patient1.pk).exists()
		)
