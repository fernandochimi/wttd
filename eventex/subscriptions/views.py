# coding: utf-8
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription
from django.views.generic import CreateView, DetailView


class SubscriptionCreateView(CreateView):
	model = Subscription
	form_class = SubscriptionForm


class SubscriptionDetailView(DetailView):
	model = Subscription