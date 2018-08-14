from django.contrib.auth.models import User
#from core.models import User


class EmailAuthBackend:
    """
    Authenticate using e-mail account.
    AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
        #'accounts.authentication.EmailAuthBackend',
        #'oauth2_provider.backends.OAuth2Backend',
        'allauth.account.auth_backends.AuthenticationBackend',
    )
    No se usa, basta con ACCOUNT_AUTHENTICATION_METHOD = 'email'
    """

    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
