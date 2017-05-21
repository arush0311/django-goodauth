from django.conf.urls import url, include
from django.urls import reverse_lazy

from . import auth_views


app_name = 'goodauth'
urlpatterns = [
	url(r'^login/$',
		auth_views.LoginView.as_view(),
		name='login'),

	url(r'^logout/$',
		auth_views.LogoutView.as_view(),
		name='logout'),

	url(r'^password_change/$',
		auth_views.PasswordChangeView.as_view(),
		name='password_change'),

	url(r'^password_reset/$',
		auth_views.PasswordResetView.as_view(),
		name='password_reset'),

	url(r'^password_reset/done/$',
		auth_views.PasswordResetDoneView.as_view(),
		name='password_reset_done'),
	
	url(r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
		auth_views.PasswordResetConfirmView.as_view(),
		name='password_reset_confirm'),

	url(r'^password_reset_complete/$',
		auth_views.PasswordResetCompleteView.as_view(),
		name='password_reset_complete'),
]
