from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView,ListView
from .models import AboutUs,Program


class HomePageView(ListView):
    template_name = 'homepage.html'
    model = Program
    context_object_name = 'programs'


class AboutUsView(ListView):
    template_name = 'about.html'
    model = AboutUs
    context_object_name = 'aboutus'