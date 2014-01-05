import kerberos
import logging

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


logger = logging.getLogger(__name__)

class KrbBackend(ModelBackend):
    """
    Django Authentication backend using Kerberos for password checking.
    """

    def authenticate(self, username=None, password=None):
        UserModel = get_user_model()
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)

        if not self.check_password(username, password):
            return None
            
        UserModel = get_user_model()
        user, created = UserModel.objects.get_or_create(**{
            UserModel.USERNAME_FIELD+"__iexact": username,
            "defaults": { UserModel.USERNAME_FIELD: username }
        })
        return user

    def check_password(self, username, password):
        """The actual password checking logic. Separated from the authenticate code from Django for easier updating"""
        try:
            kerberos.checkPassword(username.lower(), password, settings.KRB5_SERVICE, settings.KRB5_REALM)
            return True
        except kerberos.BasicAuthError:
            if getattr(settings, "KRB5_DEBUG", False):
                logger.exception("Failure during authentication")
            return False
