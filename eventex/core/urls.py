# coding: utf-8
from django.conf.urls import patterns, include, url
from eventex.core.views import HomeView, SpeakerDetailView, TalkDetailView


urlpatterns = patterns('eventex.core.views',
	url(r'^$', HomeView.as_view(), name='home'),
	url(r'^palestrantes/(?P<slug>[\w-]+)/$', SpeakerDetailView.as_view(), name='speaker_detail'),
	url(r'^palestras/$', 'talk_list', name='talk_list'),
	url(r'^palestras/(?P<pk>\d+)/$', TalkDetailView.as_view(), name='talk_detail'),
)