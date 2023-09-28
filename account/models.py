from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin,Group,Permission
from django.utils.translation import gettext_lazy as _
# Create your models here.

class UserProfileManager(BaseUserManager):
  def create_user(self,email,password=None,**extra_fields):
    if not email:
      raise ValueError("Users must have an email address")
    email=self.normalize_email(email)
    user=self.model(email=email,**extra_fields)
    user.set_password(password)
    user.save(using=self.db)
    return user
  def create_superuser(self, email, password=None, username=None):
    user = self.create_user(email=email, password=password, username=username)
    user.is_staff = True
    user.is_superuser = True
    user.save(using=self._db)
    return user



class UserProfile(AbstractBaseUser,PermissionsMixin):
    username=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserProfileManager()

  

    def __str__(self):
        return f"{self.email}-{self.id}"
    
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name='user_profile_groups'  # Use a unique related_name
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='user_profile_user_permissions'  # Use a unique related_name
    )