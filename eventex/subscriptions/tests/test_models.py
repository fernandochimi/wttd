# coding: utf-8
from django.test import TestCase
from django.db import IntegrityError
from datetime import datetime
from eventex.subscriptions.models import Subscription


class SubscriptionTest(TestCase):
	def setUp(self):
		self.obj = Subscription(
			name='Fernando',
			cpf='40090038800',
			email='fernando@chimi.com.br',
			phone='16-91515651'
		)

	def test_create(self):
		'Subscription must have name, cpf, email, phone'
		self.obj.save()
		self.assertEqual(1, self.obj.pk)

	def test_has_created_at(self):
		'Subscriptions must have automatic created_at'
		self.obj.save()
		self.assertIsInstance(self.obj.created_at, datetime)

	def test_unicode(self):
		self.assertEqual(u'Fernando', unicode(self.obj))


class SubscriptionUniqueTest(TestCase):
	def setUp(self):
		# Create a first entry to force the collision
		Subscription.objects.create(name='Fernando', cpf='40090038800',
			email='fernando@chimi.com.br', phone='16-91515651')

	def test_cpf_unique(self):
		'CPF must be unique'
		s = Subscription(name='Fernando', cpf='40090038800',
			email='fernando@chimi.com', phone='16-91515651')
		self.assertRaises(IntegrityError, s.save)

	def test_email_unique(self):
		'Email must be unique'
		s = Subscription(name='Fernando', cpf='40090038801',
			email='fernando@chimi.com.br', phone='16-91515651')
		self.assertRaises(IntegrityError, s.save)