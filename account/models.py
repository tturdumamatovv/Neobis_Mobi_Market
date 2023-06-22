from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('The email field should be set!')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        user = self.create_user(email, username, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    photo = models.ImageField(upload_to='profiles/', null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, unique=True, null=True, blank=True)

    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


class VerifyPhone(models.Model):
    phone = models.CharField(max_length=255)
    code = models.CharField(max_length=255, unique=True)


class Product(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    photo = models.ImageField(upload_to='products/', null=True, blank=True)
    description = models.TextField()
    likes = models.ManyToManyField(CustomUser, through='ProductLike', related_name='liked_product')

    def __str__(self):
        return self.name

    @property
    def like_count(self):
        return self.product_likes.count()


class ProductLike(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_likes')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['product', 'user']


