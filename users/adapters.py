from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.exceptions import ImmediateHttpResponse
from django.http import HttpResponse


class MySocialAccountAdapter(DefaultSocialAccountAdapter):

    def pre_social_login_x(self, request, sociallogin):
        email_domain = sociallogin.user.email.split('@')[1].lower()
        if not email_domain == 'upeu.edu.pe':
            print (email_domain)
            raise ImmediateHttpResponse(HttpResponse(
                sociallogin.user.email + ' is not valid memeber of upeu.edu.pe'))
        else:
            pass

    def save_user(self, request, sociallogin, form=None):
        print ("DefaultSocialAccountAdapter.save_user")

        user = super(MySocialAccountAdapter, self).save_user(
            request, sociallogin, form
        )

        # Add your own processing here.
        print (sociallogin.user.email)
        user.email = sociallogin.user.email
        user.is_staff = True
        user.save()

        # You must return the original result.
        return user
