# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
	def test_has_fields(self):
		'Form must be have 4 fields'
		form = SubscriptionForm()
		self.assertItemsEqual(['name', 'email', 'cpf', 'phone'], form.fields)

	def test_cpf_is_digit(self):
		'CPF must be accept digits'
		form = self.make_validated_form(cpf='ABCD0038800')
		self.assertItemsEqual(['cpf'], form.errors)

	def test_cpf_has_11_digits(self):
		'CPF must be accept 11 digits'
		form = self.make_validated_form(cpf='1234')
		self.assertItemsEqual(['cpf'], form.errors)

	def test_email_is_optional(self):
		'Email is optional'
		form = self.make_validated_form(email='')
		self.assertFalse(form.errors)

	def test_must_inform_email_or_phone(self):
		'Email and phone are optional, but must be informed'
		form = self.make_validated_form(email='', phone_0='', phone_1='')
		self.assertItemsEqual(['__all__'], form.errors)

	def test_name_must_be_capitalized(self):
		'Name must be capitalized'
		form = self.make_validated_form(name='FERNANDO chimi')
		self.assertEqual('Fernando Chimi', form.cleaned_data['name'])

	def make_validated_form(self, **kwargs):
		data = dict(name='Fernando Chimi', email='fernando@chimi.com.br',
			cpf='40090038800', phone_0='16', phone_1='91515651')
		data.update(kwargs)
		form = SubscriptionForm(data)
		form.is_valid()
		return form