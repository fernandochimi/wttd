# coding: utf-8
from unittest import skip
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.test.utils import override_settings
from eventex.myauth.backends import EmailBackend


@skip
class EmailBackendTest(TestCase):
	def setUp(self):
		UserModel = get_user_model()
		UserModel.objects.create_user(username='fernando',
			                          email='fernando@chimi.com.br',
			                          password='goiabada')
		self.backend = EmailBackend()

	def test_authenticate_with_email(self):
		user = self.backend.authenticate(email='fernando@chimi.com.br',
			                             password='goiabada')
		self.assertIsNotNone(user)

	def test_wrong_password(self):
		user = self.backend.authenticate(email='fernando@chimi.com.br',
			                             password='goiaba')
		self.assertIsNone(user)

	def test_unknown_user(self):
		user = self.backend.authenticate(email='fernando@chimicoviaki.com.br',
			                             password='goiabada')
		self.assertIsNone(user)

	def test_get_user(self):
		self.assertIsNotNone(self.backend.get_user(1))


@skip
class MultipleEmailsTest(TestCase):
	def setUp(self):
		UserModel = get_user_model()
		UserModel.objects.create_user(username='user1',
			email='fernando@chimi.com.br', password='goiabada')
		UserModel.objects.create_user(username='user2',
			email='fernando@chimi.com.br', password='goiabada')
		self.backend = EmailBackend()

	def test_multiple_emails(self):
		user = self.backend.authenticate(email='fernando@chimi.com.br',
			                             password='goiabada')
		self.assertIsNone(user)


@skip
@override_settings(AUTHENTICATION_BACKENDS=('eventex.myauth.backends.EmailBackend',))
class FunctionalEmailBackendTest(TestCase):
	def setUp(self):
		UserModel = get_user_model()
		UserModel.objects.create_user(username='fernando',
			                          email='fernando@chimi.com.br',
			                          password='goiabada')

	def test_login_with_email(self):
		result = self.client.login(email='fernando@chimi.com.br',
			                       password='goiabada')
		self.assertTrue(result)

	def test_login_with_username(self):
		result = self.client.login(username='fernando@chimi.com.br',
			                       password='goiabada')
		self.assertTrue(result)