from django.urls import path

from .views import SignupPageView, CustomPasswordChangeView

urlpatterns = [
    path("signup/", SignupPageView.as_view(), name="signup"),
    path("password/change/", CustomPasswordChangeView.as_view(), name='account_change_password'),
]