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


