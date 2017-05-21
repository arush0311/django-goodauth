from django.urls import reverse, reverse_lazy
from django.contrib.auth import views as django_auth_views
from django.utils.http import is_safe_url
from django.contrib import messages
from django.shortcuts import resolve_url
from django.conf import settings


class LoginView(django_auth_views.LoginView):

    template_name='goodauth/login.html'
    redirect_authenticated_user=True


class LogoutView(django_auth_views.LogoutView):
    next_page = reverse_lazy('goodauth:login')


class PasswordChangeView(django_auth_views.PasswordChangeView):
    template_name = 'goodauth/password_change.html'
    success_url = settings.LOGIN_REDIRECT_URL

class PasswordResetView(django_auth_views.PasswordResetView):
    template_name = 'goodauth/password_reset.html'
    email_template_name = 'goodauth/password_reset_email_body.html'
    subject_template_name = 'goodauth/password_reset_email_subject.html'
    success_url = reverse_lazy('goodauth:password_reset_done')

class PasswordResetDoneView(django_auth_views.PasswordResetDoneView):
    template_name = 'goodauth/password_reset_done.html'


class PasswordResetConfirmView(django_auth_views.PasswordResetConfirmView):
    template_name = 'goodauth/password_reset_confirm.html'
    success_url = reverse_lazy('goodauth:password_reset_complete')


class PasswordResetCompleteView(django_auth_views.PasswordResetCompleteView):
    template_name = 'goodauth/password_reset_complete.html'