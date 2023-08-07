from django.urls import reverse_lazy
from django.views import generic
from allauth.account.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CustomUserCreationForm

class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    success_url = reverse_lazy("home")