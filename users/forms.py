from allauth.socialaccount.forms import SignupForm


class MyCustomSocialSignupForm(SignupForm):

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
        #user.set_password(self.user, self.cleaned_data["password1"])
        user.is_staff = True
        user.save()
    '''
