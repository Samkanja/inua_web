from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView,ListView
from .models import AboutUs


class HomePageView(TemplateView):
    template_name = 'index.html'


class AboutUsView(ListView):
    template_name = 'about.html'
    model = AboutUs
    context_object_name = 'aboutus'