from .views import UserRegistrationView
from django.urls import path
from django.contrib.auth import views as auth_views
app_name = 'users'

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='admin/login.html',redirect_authenticated_user=True),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='admin/logout.html'),name='logout'),
]   