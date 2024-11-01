from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class Indexview(TemplateView):
    template_name = 'index.html'


class Premiumview(TemplateView):
    template_name = 'premium.html'

class Helpview(TemplateView):
    template_name = 'help.html'

class Downloadview(TemplateView):
    template_name = 'download.html'


class SongsView(TemplateView):
    template_name = 'songs.html'

