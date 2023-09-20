from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import UserRegistrationForm

class UserRegistrationView(FormView):
    template_name = 'admin/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')

    def form_valid(self,form):
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(self.request,f'Acount Create for {username}')
        return super().form_valid(form)