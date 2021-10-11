from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.



# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self,username, email, password=None):
        if not email:
            raise ValueError("Email is Required")
        

        user=self.model(
            email = self.normalize_email(email),
            username = username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            username = username,
            email=email,
            password = password
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff= True
        user.save(using=self._db)
        return user



class UserProfile(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True, blank=False)
    email =models.EmailField(verbose_name="email address", max_length=50, unique=True, blank=False)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    phone = models.CharField(max_length=15, verbose_name="phone")
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active= models.BooleanField(default=True)
    is_staff= models.BooleanField(default=False)
    is_superuser= models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)


    USERNAME_FIELD="username"

    REQUIRED_FIELDS=['email']

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app__label):
        return True