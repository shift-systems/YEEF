from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from django.db import models
from django.utils import timezone
import uuid

ID_LENGTH = 9


def id_gen() -> str:
    """Generates random string whose length is `ID_LENGTH`"""
    return str(uuid.uuid4())[:ID_LENGTH]


class UserManager(BaseUserManager):
    def create_user(self, **kwargs):
        """
        Creates and saves a User with the given credentials.
        """
        email = kwargs.get("email")
        password = kwargs.get("password")
        mobile_number = kwargs.get("mobile_number")

        user = self.model.objects.filter(email=email).first()
        user_mobile_number = \
            self.model.objects.filter(mobile_number=mobile_number).first()
        if user_mobile_number:
            raise ValueError(
                "User with mobile number {mobile_number} "
                "already exists".format(mobile_number=mobile_number)
            )
        if user:
            raise ValueError(
                "User with email {email} already exists".format(email=email)
            )
        user = self.model(
            mobile_number=mobile_number, email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password)
        user.is_superuser = user.is_staff = True
        user.is_active = user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
        User model
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    password = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=100, null=True, unique=True)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_admin_permission(self, perm, obj=None):
        return self.is_admin

    def has_module_permission(self, app_label):
        return self.is_admin

    def has_super_admin_permission(self, perm, obj=None):
        return self.is_superuser

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self):
        super().delete()


class Profile(models.Model):
    """
        User Role model
    """
    profile = models.OneToOneField(
        "User",
        null=True, blank=True,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=50, unique=True
    )
    profile_image = models.URLField(
        default='https://res.cloudinary.com/du3v7gyou/image/upload/v1567601646/yeef/Profile_Picture_Placeholder_qqwprt.png'
    )
    job_title = models.CharField(max_length=100, null=True, blank=True)
    starting_date = models.DateField(blank=True, null=True)
    birthday = models.DateField(auto_now=False, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Roles"
        ordering = ("name",)

    def __str__(self):
        return self.name


class Role(models.Model):
    """
        User Role model
    """

    name = models.CharField(
        max_length=50, unique=True
    )

    class Meta:
        verbose_name_plural = "Roles"
        ordering = ("name",)

    def __str__(self):
        return self.name
