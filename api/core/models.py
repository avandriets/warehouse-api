import uuid
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class CommonInfo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        User,
        on_delete=models.RESTRICT,
        related_name='%(app_label)s_%(class)s_related',
        null=True,
    )

    class Meta:
        abstract = True


class Catalogue(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='updated_by_user', null=True)


class UnitOfMeasures(CommonInfo):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    shortName = models.CharField(max_length=10, unique=True)
    description = models.CharField(max_length=255)


class Store(CommonInfo):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255)


class PriceTypes(CommonInfo):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255)


class Customers(CommonInfo):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255)
    tax_number = models.CharField(max_length=100, unique=True)
    seller = models.BooleanField()
    description = models.CharField(max_length=255)


class Products(CommonInfo):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    printName = models.CharField(max_length=255)
    barcode = models.CharField(max_length=100)
    category = models.ForeignKey(Catalogue, on_delete=models.RESTRICT)
    product_code = models.CharField(max_length=255)
    height = models.FloatField()
    width = models.FloatField()
    length = models.FloatField()
    weight = models.FloatField()
    description = models.CharField(max_length=255)


class Settings(CommonInfo):
    current_company = models.ForeignKey(Catalogue, on_delete=models.RESTRICT)
