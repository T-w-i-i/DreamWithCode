from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import View


class HomeView(TemplateView):
    template_name = 'dwcsite/index.html'

class AboutView(TemplateView):
    template_name = 'dwcsite/about.html'
