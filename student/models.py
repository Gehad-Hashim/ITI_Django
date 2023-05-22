from django.db import models

# Create your models here.
class student(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    age=models.IntegerField(max_length=3)