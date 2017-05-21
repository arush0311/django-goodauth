Plug and play django authentication
-----------------------------------

This is one concrete implementation of django auth which
covers common use cases of authentication.

Just include this app and authentication will be taken care for you.

Installation and Configuration
------------------------------

Install django-goodauth package 
```
pip install git+https://github.com/arush0311/django-goodauth
```

Include `goodauth` and `bootstrap3` in installed apps in `settings.py` of your django project
```
INSTALLED_APPS = [
	...
    'bootstrap3',
    'goodauth',
    ...
]

```

Specify following config options in `settings.py`

```
# Full path of URL to redirect to after login.
# It is most probably the homepage of your logged in users.
LOGIN_REDIRECT_URL = '/home/'

# Full path of URL where the login page will be displayed.
# If you mount goodauth at `X`, the login page will be at `X/login/`
LOGIN_URL = '/custom_auth/login/'


# Email specification for sending emails for `forgot_password`.
# For more information see https://docs.djangoproject.com/en/1.11/topics/email/
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'someone@gmail.com'
EMAIL_HOST_PASSWORD = '*************'
EMAIL_USE_SSL = True
EMAIL_PORT = 465
EMAIL_TIMEOUT = 3
```

Mount goodauth
```
# urls.py
from django.conf.urls import url, include

urlpatterns = [
	...
    url(r'^custom_auth/', include('goodauth.urls')),
    ...
]
```

Enjoy!!

Authentication URLs
-------------------
If `x` is the mount point:

/x/login/$ 				[name='goodauth:login']
/x/logout/$ 			[name='goodauth:logout']
/x/password_change/$ 	[name='goodauth:password_change']
/x/password_reset/$ 	[name='goodauth:password_reset']
