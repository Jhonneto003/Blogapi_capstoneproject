from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from .managers import CustomUserManager

# Create your models here.
class CustomUser(AbstractUser):
    email=models.EmailField(unique=True)
    username=models.CharField(max_length=100, unique=True)
    date_of_birth=models.DateField(null=True,blank=True)
    last_name = models.CharField(max_length=150, blank=True, default='') 
    date_joined=models.DateTimeField(default=timezone.now)
    # is_active=models.BooleanField(default=True)
    # is_staff=models.BooleanField(default=False)
    # first_name= models.CharField(max_length=50, null=True,blank=True)
    # last_name= models.CharField(max_length=50, unique=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()
    
    def __str__(self) -> str:
        return self.email

# Create your models here.
