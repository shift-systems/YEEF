

import uuid

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from django.utils import timezone

from ...models import BaseModel
from .users import User


class Role(models.Model):
    name = models.CharField(max_length=30)


class Profile(BaseModel):
    user = models.OneToOneField(
        User, related_name='person', on_delete=models.CASCADE)
    bio = models.TextField()
    role = models.ManyToManyField(Role)
