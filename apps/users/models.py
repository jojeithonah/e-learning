from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext as _
from common import enums


class User(AbstractUser):
    USER_TYPE = (
        (enums.UserRole.SUPER_ADMIN.value, _('Super Admin')),
        (enums.UserRole.TEACHER.value, _('Teacher')),
        (enums.UserRole.STUDENT.value, _('Student')),
    )
    type = models.IntegerField(
        choices=USER_TYPE,
        verbose_name=_('Rol'),
        default=enums.UserRole.STUDENT.value
    )
    full_name = models.CharField(
        max_length=255,
        verbose_name=_('Full Name'),
        )

    email = models.EmailField(
        max_length=255, 
        unique=True,
        verbose_name=_('Email'),
        )
    username = models.CharField(
        max_length=255,
        verbose_name=_('Username'),
        )
  
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created At'),
        )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Updated At'),

        )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'type', 'full_name']

    def __str__(self):
        return "{}".format(self.full_name)


    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
