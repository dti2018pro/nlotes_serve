from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from allauth.account.forms import SignupForm
from django import forms
from django.utils.translation import pgettext, ugettext, ugettext_lazy as _


class MyCustomSocialSignupForm(SocialSignupForm):

    def save(self, request):

        # Ensure you call the parent classes save.
        # .save() returns a User object.
        # self.fields['is_staff'] = True
        print ("hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")

        user = super(MyCustomSocialSignupForm, self).save(request)

        # Add your own processing here.
        user.is_staff = True
        user.save()

        # You must return the original result.
        return user
    '''

    def signup(self, request, user):
        print ("hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
        # user.set_password(self.user, self.cleaned_data["password1"])
        user.is_staff = True
        user.save()
    '''


class MyCustomSignupForm(SignupForm):
    email = forms.CharField(label=_("Email"),
                            widget=forms.TextInput(
        attrs={'placeholder':
               _('Email'),
               'autofocus': 'autofocus'}),
        required=False)
    first_name = forms.CharField(
        max_length=300, label=_('first name'), required=False)
    last_name = forms.CharField(
        max_length=300, label=_('last name'), required=False)

    def save(self, request):
        print ("xxxxxxxxxxxxxxxxxxx MyCustomSignupForm xxxxxxxxxxxxxxxxx")
        # Ensure you call the parent classes save.
        # .save() returns a User object.
        user = super(MyCustomSignupForm, self).save(request)

        # Add your own processing here.
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.is_staff = True
        user.save()
        # You must return the original result.
        return user

from django.contrib.auth import get_user_model


class SignupForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name']

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.is_staff = True
        user.save()


class MyCustomSignupFormx(SignupForm):
    username = forms.CharField(label=_("Username"),

                               widget=forms.TextInput(
                                   attrs={'placeholder':
                                          _('Username'),
                                          'autofocus': 'autofocus'}))

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.is_staff = True
        user.save()
