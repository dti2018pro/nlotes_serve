from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser
#from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

'''
class Profile(models.Model):
    OTHER = 0
    NID = 1
    FOREING_CARD = 2
    CERTIFICATE_BIRTH = 3
    IDENTITY_TYPE_CHOICES = (
        (NID, _('n.i.d.')),
        (FOREING_CARD, _('foreign card')),
        (CERTIFICATE_BIRTH, _('certificate birth')),
        (OTHER, _('other')),
    )
    # id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    identity_type = models.PositiveSmallIntegerField(
        choices=IDENTITY_TYPE_CHOICES, default=NID, null=True, blank=True)
    identity_num = models.CharField(
        _('identity num'), max_length=20, null=True, blank=True)
    location = models.CharField(
        _('location'), max_length=30, null=True, blank=True)
    birth_date = models.DateField(_('birth date'), null=True, blank=True)
    photo = models.ImageField(
        _('photo'), upload_to='persons', default='persons/default.png',
        blank=True)

    detail = models.TextField(verbose_name=_('detail'), null=True, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


'''


class Person(models.Model):
    OTHER = 0
    NID = 1
    FOREING_CARD = 2
    CERTIFICATE_BIRTH = 3
    IDENTITY_TYPE_CHOICES = (
        (NID, _('n.i.d.')),
        (FOREING_CARD, _('foreign card')),
        (CERTIFICATE_BIRTH, _('certificate birth')),
        (OTHER, _('other')),
    )
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    identity_type = models.PositiveSmallIntegerField(
        _('identity type'), choices=IDENTITY_TYPE_CHOICES, default=NID,
        null=True, blank=True)
    identity_num = models.CharField(
        _('identity num'), max_length=20, null=True, blank=True)

    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), blank=True)
    is_active = models.BooleanField(_('active'), default=True)
    birth_date = models.DateField(_('birth date'), null=True, blank=True)
    photo = models.ImageField(
        _('photo'), upload_to='persons', default='persons/default.png',
        blank=True)

    created = models.DateTimeField(_('created'), auto_now_add=True, blank=True)
    modified = models.DateTimeField(_('modified'), auto_now=True, blank=True)

    class Meta:
        verbose_name = _('person')
        verbose_name_plural = _('persons')
        unique_together = (
            ('first_name', 'last_name', 'identity_type', 'identity_num'),
            ('identity_type', 'identity_num'),
        )

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name, )


class User(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    person = models.OneToOneField(
        'Person', on_delete=models.CASCADE, verbose_name=_('person'),
        null=True, blank=True)
    detail = models.TextField(_('detail'), blank=True)
    last_did = models.CharField(
        _('last did'), max_length=250, null=True, blank=True)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return '%s' % (self.username)

'''
@receiver(post_save, sender=User)
def create_or_update_user_person(sender, instance, created, **kwargs):
    if created:
        Person.objects.create(user=instance)
    instance.person.save()
'''
