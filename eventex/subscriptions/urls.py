# coding: utf-8
from django.conf.urls import patterns, include, url
from eventex.subscriptions.views import SubscriptionDetailView, SubscriptionCreateView

	
urlpatterns = patterns('eventex.subscriptions.views',
	url(r'^$', SubscriptionCreateView.as_view(), name='subscribe'),
	url(r'^(?P<pk>\d+)/$', SubscriptionDetailView.as_view(), name='detail'),
)