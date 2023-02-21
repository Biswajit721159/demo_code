from django.db import models

# Create your models here.

class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    catagory=models.CharField(max_length=50,default="")
    subcatagory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300)
    put_date=models.DateField()
    image=models.ImageField(upload_to="shop/images",default="")
    rating=models.IntegerField(default=1)


    def __str__(self):
      return self.product_name    

class Photo(models.Model):
  photo=models.ImageField(upload_to='photo/images')



class order(models.Model):
  username=models.CharField(max_length=20)
  orderid=models.IntegerField()
  