from django.urls import path
from .views import HomePageView,AboutUsView

app_name = 'main'
urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('about/',AboutUsView.as_view(),name='aboutus'),
]