# coding- utf-8
from django.test import TestCase
from eventex.subscriptions.models import Subscription
from django.core.urlresolvers import reverse as r


class DetailTest(TestCase):
	def setUp(self):
		s = Subscription.objects.create(name='Fernando', cpf='40090038800',
			email='fernando@chimi.com.br', phone='16-91515651')
		self.resp = self.client.get(r('subscription:detail', args=[s.pk]))

	def test_get(self):
		'GET /inscricao/1/ should return status 200'
		self.assertEqual(200, self.resp.status_code)

	def test_template(self):
		'Uses template'
		self.assertTemplateUsed(self.resp,
			'subscriptions/subscription_detail.html')

	def test_context(self):
		'Context must have a subscription instance'
		subscription = self.resp.context['subscription']
		self.assertIsInstance(subscription, Subscription)

	def test_html(self):
		'Check if subscription data was rendered'
		self.assertContains(self.resp, 'Fernando')


class DetailNotFound(TestCase):
	def test_not_found(self):
		response = self.client.get(r('subscription:detail', args=[0]))
		self.assertEqual(404, response.status_code)