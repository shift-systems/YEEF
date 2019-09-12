

import uuid

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from django.utils import timezone

from ...models import BaseModel
from .users import User
from api.utils.id_generatory import id_gen, ID_LENGTH


class Role(models.Model):
    id = models.CharField(
        max_length=ID_LENGTH, primary_key=True, default=id_gen, editable=False
    )
    name = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.name

    def __str__(self):
        return self.name


class Profile(BaseModel):
<<<<<<< HEAD
    id = models.CharField(
        max_length=ID_LENGTH, primary_key=True, default=id_gen, editable=False
    )
    user = models.OneToOneField(
        User, related_name='person', on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    role = models.ManyToManyField(Role, blank=True)
    avatar = models.URLField()

    def __str__(self):
        return f'< {str(self.user)}:{str(self.role.name)}>'
=======
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        User, related_name='person', on_delete=models.CASCADE)
    bio = models.TextField()
    role = models.ManyToManyField(Role)
    avatar = models.URLField()

    def __str__(self):
        return f'< {str(self.user)}:{str(self.role)}>'
>>>>>>> athentication
