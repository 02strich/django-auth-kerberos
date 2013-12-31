django-auth-kerberos
====================

Kerberos authentication backend for Django

Install
-------

    pip install django-auth-kerberos

Usage
-----

Make sure following settings are configured in `settings.py`:

    INSTALLED_APPS = (
        ...
        'django_auth_kerberos',
        ...
    )

    # kerberos realm and service
    KRB5_REALM = 'EXAMPLE.COM'
    KRB5_SERVICE = 'krbtgt@AS.EXAMPLE.COM'

    # redirect url after login
    LOGIN_REDIRECT_URL = '/'

    # enable kerberos auth backends
    AUTHENTICATION_BACKENDS = (
        'django_auth_kerberos.backends.KrbBackend',
    )
