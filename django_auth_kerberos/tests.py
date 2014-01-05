import unittest

from django.conf import settings

from django_auth_kerberos.backends import KrbBackend

class BasicTest(unittest.TestCase):
	def setUp(self):
		self.sut = KrbBackend()

	def test_login_success(self):
		self.assertIsNotNone(self.sut.authenticate(settings.KRB5_TEST_USER, settings.KRB5_TEST_PASSWORD))

	def test_login_wrong_password(self):
		self.assertIsNone(self.sut.authenticate('asdafasd', ''))
