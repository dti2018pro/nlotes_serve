from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
#from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
#from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Person, User

admin.site.register(Person)

'''
class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = User
'''


class CustomUserAdmin(UserAdmin):
    '''
    #add_form = UserCreationForm
    #form = UserChangeForm
    #model = User
    fieldsets = (
        (None, {'fields': ('username', 'password',
                           'email', 'first_name', 'last_name')}),
        (_('Personal info'),
         {'fields': ('person', )}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff',
                                       'is_superuser', 'groups',
                                       'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    '''
    fieldsets = UserAdmin.fieldsets + (

        (_('Personal info'),
         {'fields': ('person', )}),

    )
    raw_id_fields = ('person',)


admin.site.register(User, CustomUserAdmin)

'''
class ProfileInline(admin.StackedInline):
    model = Person
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username', 'email', 'first_name',
                    'last_name', 'is_staff', 'get_location')
    list_select_related = ('profile', )

    def get_location(self, instance):
        return instance.profile.location
    #get_location.short_description = 'Location'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
'''
