import uuid
from datetime import datetime, timedelta

import jwt
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from django.utils import timezone
from django.conf import settings
from api.utils.id_generatory import id_gen, ID_LENGTH


class UserManager(BaseUserManager):

    def create_user(self, **kwargs):
        """Create and return a `User` with an email,mobile number, username and password."""

        email = kwargs.get("email")
        password = kwargs.get("password")
        mobile_number = kwargs.get("mobile_number")

        user = self.model.objects.filter(email=email).first()
        user_mobile_number = \
            self.model.objects.filter(mobile_number=mobile_number).first()
        if user_mobile_number:
            raise ValueError(
                f"User with mobile number {mobile_number} "
                "already exists"
            )
        if user:
            raise ValueError(
                f"User with email {email} already exists"
            )
        user = self.model(
            mobile_number=mobile_number, email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password):
        """
          Create and return a `User` with superuser powers.
          Superuser powers means that this use is an admin that can do anything
          they want.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(
            email=email, username=username, password=password,
            mobile_number='256788088831')
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    User model
    """

    id = models.CharField(
        max_length=ID_LENGTH, primary_key=True, default=id_gen, editable=False
    )
    password = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=100, null=True, unique=True)
    username = models.CharField(
        db_index=True, max_length=255, unique=True, null=True)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

    """
    More fields required by Django when specifying a custom user model.
    The `USERNAME_FIELD` property tells us which field we will use to log in.
    In this case, we want that to be the email field.
    """
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    """
    Tells Django that the UserManager class defined above should manage
    objects of this type.
    """
    objects = UserManager()

    def __str__(self):
        """
        Returns a string representation of this `User`
        """
        return self.email

    @property
    def token(self):
        """
        Generate and return  a jwt token. The user's unique id and username
        are the user details encode within the user token.
        """
        expire_date = datetime.now() + timedelta(days=0, hours=24)
        token = jwt.encode({
            'id': str(self.id),
            'email': self.email,
            'exp': expire_date,
        }, settings.SECRET_KEY, algorithm="HS256"
        )
        return token.decode('utf-8')

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self):
        super().delete()
