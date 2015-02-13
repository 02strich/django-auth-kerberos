try:
    import kerberos
except ImportError:
    import kerberos_sspi as kerberos
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
        if getattr(settings, "KRB5_CREATE_USER", True):
            if getattr(settings, "KRB5_USERNAME_MATCH_IEXACT", True):
                user, created = UserModel.objects.get_or_create(**{
                    UserModel.USERNAME_FIELD+"__iexact": username,
                    "defaults": { UserModel.USERNAME_FIELD: username }
                })
                return user
            else:
                user, created = UserModel.objects.get_or_create(**{
                    UserModel.USERNAME_FIELD: username,
                    "defaults": { UserModel.USERNAME_FIELD: username }
                })
                return user
        else:
            try:
                if getattr(settings, "KRB5_USERNAME_MATCH_IEXACT", True):
                     return UserModel.objects.get(**{UserModel.USERNAME_FIELD+"__iexact": username})
                else:
                    return UserModel._default_manager.get_by_natural_key(username)
            except UserModel.DoesNotExist:
                return None
        return None

    def check_password(self, username, password):
        """The actual password checking logic. Separated from the authenticate code from Django for easier updating"""
        try:
            kerberos.checkPassword(username.lower(), password, getattr(settings, "KRB5_SERVICE", ""), settings.KRB5_REALM)
            return True
        except kerberos.BasicAuthError:
            if getattr(settings, "KRB5_DEBUG", False):
                logger.exception("Failure during authentication")
            return False
        except:
            if getattr(settings, "KRB5_DEBUG", False):
                logger.exception("Failure during authentication")
            # for all other execptions also deny access
            return False
