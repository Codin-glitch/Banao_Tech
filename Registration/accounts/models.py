from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    USER_CHOICES = (
        ('patient', 'Patient'),
        ('doctor', 'Doctor')
    )

    user_type = models.CharField(max_length=10, choices=USER_CHOICES, default = 'patient')

    email = models.EmailField(unique=True)

    profile_picture = models.ImageField(upload_to="profile")
    address_line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)

