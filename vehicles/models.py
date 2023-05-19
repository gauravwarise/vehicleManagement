from django.db import models

# Create your models here.
from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User  
# Create your models here.

class Vehicle(models.Model):
    vehicle_number = models.CharField(max_length=100)
    vehicle_type = models.CharField(
        choices = (
        ("Two Wheelers","Two Wheelers"),
        ("Three Wheelers","Three Wheelers"),
        ("Four Wheelers","Four Wheelers")
        ),
        max_length=100
    )
    vehicle_model = models.CharField(max_length=100)
    vehicle_description = models.TextField()

    class Meta:
        db_table = "vehicle"

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = "__all__"

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']