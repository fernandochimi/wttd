# coding: utf-8
from django.test import TestCase
from django.core.exceptions import ValidationError
from eventex.core.models import Speaker, Contact


class SpeakerModelTest(TestCase):
	def setUp(self):
		self.speaker = Speaker(name='Fernando Chimi',
			                   slug='fernando-chimi',
			                   url='http://chimiapp.heroku.com',
			                   description='Blablabla')
		self.speaker.save()

	def test_create(self):
		'Speaker instance should be saved'
		self.assertEqual(1, self.speaker.pk)

	def test_unicode(self):
		'Speaker string representation should be the name.'
		self.assertEqual(u'Fernando Chimi', unicode(self.speaker))


class ContactModelTest(TestCase):
	def setUp(self):
		self.speaker = Speaker.objects.create(name='Fernando Chimi',
			slug='fernando-chimi', url='http://chimiapp.heroku.com',
			description='Blablabla')

	def test_email(self):
		contact = Contact.objects.create(speaker=self.speaker, kind='E',
			value='fernando@chimi.com.br')
		self.assertEqual(1, contact.pk)

	def test_phone(self):
		contact = Contact.objects.create(speaker=self.speaker, kind='P',
			value='16-991515651')
		self.assertEqual(1, contact.pk)

	def test_fax(self):
		contact = Contact.objects.create(speaker=self.speaker, kind='F',
			value='16-12345678')
		self.assertEqual(1, contact.pk)

	def test_kind(self):
		'Contact kind should be limited to E, P or F'
		contact = Contact(speaker=self.speaker, kind='A', value='B')
		self.assertRaises(ValidationError, contact.full_clean)

	def test_unicode(self):
		'Contact string representation should be value'
		contact = Contact(speaker=self.speaker, kind='E',
			value='fernando@chimi.com.br')
		self.assertEqual(u'fernando@chimi.com.br', unicode(contact))