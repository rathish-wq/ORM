# Ex01 Django ORM Web Application
## Date: 02.02.26

## AIM
To develop a Django Application to store and retrieve data from a E-Commerce Website Database for Amazon or Flipkart using Object Relational Mapping(ORM).


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Detect changes and create migration files that describe how to modify the database schema

### STEP 5:
Execute the migration files and update the database schema to match your Django models

### STEP 6:
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7:
Apply the migration files of the created app to the database

### STEP 8:
Execute Django admin using localhost and create details for 10 entries

## PROGRAM
```
MODELS.PY
from django.contrib import admin
from django.db import models
class ZOMATODB(models.Model):
    product_ID=models.IntegerField(primary_key=True)
    product_Name=models.CharField(max_length=25)
    hotel_Name=models.CharField(max_length=25)
    product_Price=models.IntegerField()
    hotel_Rating=models.IntegerField()
    product_category=models.CharField(max_length=20)
    product_feedback=models.TextField()
class ZOMATODBAdmin(admin.ModelAdmin):
    list_display=['product_ID','product_Name','hotel_Name','product_Price','hotel_Rating','product_category','product_feedback']




ADMIN.PY
from django.contrib import admin
from .models import ZOMATODB,ZOMATODBAdmin
admin.site.register(ZOMATODB,ZOMATODBAdmin)
```


## OUTPUT

![alt text](<Screenshot (17).png>)

## RESULT
Thus the program for creating E-commerce website database using ORM hass been executed successfully
