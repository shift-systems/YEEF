

import uuid

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from django.utils import timezone

from ...models import BaseModel
from .users import User


class Role(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Profile(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        User, related_name='person', on_delete=models.CASCADE)
    bio = models.TextField()
    role = models.ManyToManyField(Role)
    avatar = models.URLField()

    def __str__(self):
        return f'< {str(self.user)}:{str(self.role)}>'
