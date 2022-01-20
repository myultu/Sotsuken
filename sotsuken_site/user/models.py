from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.core.validators import MinLengthValidator, RegexValidator
from django.urls import reverse

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            username=username,
        )
        user.set_password(password)
        slug = username
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        slug = 'superuser'
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        verbose_name='username',
        unique=True,
        max_length=20,
        help_text='Required. 20 characters or fewer. Letters, digits and @/./+/-/_ only.',
        validators=[MinLengthValidator(3,), RegexValidator(r'^[a-zA-Z0-9]*$',)],
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    slug = models.SlugField(null=False, unique=True, default='empty')
    
    
    objects = UserManager()
    
    USERNAME_FIELD = 'username'
    
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.username
    
    def get_absolute_url(self):
      return reverse('user:user_index', kwargs={'slug': self.slug})