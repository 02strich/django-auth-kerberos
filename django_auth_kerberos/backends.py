import kerberos

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class KrbBackend(ModelBackend):
    """
    Django Authentication backend using Kerberos for password checking.
    """

    def authenticate(self, username=None, password=None):
        UserModel = get_user_model()
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        try:
            user = UserModel._default_manager.get_by_natural_key(username)
            if self.check_password(user, password):
                return user
        except UserModel.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a non-existing user (#20760).
            UserModel().set_password(password)

    def check_password(self, user, password):

        try:
            kerberos.checkPassword(username, password, settings.KRB5_SERVICE, settings.KRB5_REALM)

            return True
        except kerberos.BasicAuthError:
            return False
