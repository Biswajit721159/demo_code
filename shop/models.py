from django.db import models

# Create your models here.

class User(models.Model):
  user_id=models.IntegerField(primary_key=True)
  username=models.CharField(max_length=200)
  email=models.EmailField(max_length=254)
  password=models.CharField(max_length=20)
  phone_no=models.CharField(max_length=10)
  isAdmin=models.BooleanField(default=False)
  isOwner=models.BooleanField(default=False)

class Property(models.Model):
    property_id=models.IntegerField(primary_key=True)
    user_id=models.IntegerField()
    city=models.CharField(max_length=25)
    address=models.CharField(max_length=200)
    property_type=models.CharField(max_length=50)
    rent_amount=models.IntegerField()
    status=models.CharField(max_length=25)
    bond=models.CharField(max_length=50)
    img=models.CharField(max_length=200)
    area=models.IntegerField()
    about=models.CharField(max_length=100)
    parking=models.CharField(max_length=10)
    floor=models.CharField(max_length=20)

class Reviews(models.Model):
    rating_id=models.IntegerField(primary_key=True)
    property_id=models.IntegerField()
    comments=models.CharField(max_length=200)
    rating=models.IntegerField()
    timeperiod=models.IntegerField()

class RentedTable(models.Model):
    user_id=models.IntegerField()
    property_id=models.IntegerField()