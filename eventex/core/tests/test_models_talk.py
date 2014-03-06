# coding: utf-8
from django.test import TestCase
from eventex.core.models import Talk, Course
from eventex.core.managers import PeriodManager


class TalkModelTest(TestCase):
	def setUp(self):
		self.talk = Talk.objects.create(
			title=u'Django Intro',
			description=u'Palestra',
			start_time='10:00')

	def test_create(self):
		self.assertEqual(1, self.talk.pk)

	def test_unicode(self):
		self.assertEqual(u'Django Intro', unicode(self.talk))

	def test_speakers(self):
		'Talk has many Speakers and vice-versa'
		self.talk.speakers.create(name='Fernando Chimi',
			                      slug='fernando-chimi',
			                      url='http://chimiapp.heroku.com')
		self.assertEqual(1, self.talk.speakers.count())

	def test_period_manager(self):
		'Talk default manager must be instance of PeriodManager'
		self.assertIsInstance(Talk.objects, PeriodManager)


class CourseModelTest(TestCase):
	def setUp(self):
		self.course = Course.objects.create(title=u'Django Tutorial', 
			description=u'Descrição', start_time='10:00', slots=20)

	def test_create(self):
		self.assertEqual(1, self.course.pk)

	def test_unicode(self):
		self.assertEqual(u'Django Tutorial', unicode(self.course))

	def test_speakers(self):
		'Course has many Speakers and vice-versa'
		self.course.speakers.create(name='Fernando Chimi',
			                        slug='fernando-chimi',
			                        url='http://chimiapp.heroku.com')
		self.assertEqual(1, self.course.speakers.count())

	def test_period_manager(self):
		'Course default manager must be instance of PeriodManager'
		self.assertIsInstance(Course.objects, PeriodManager)