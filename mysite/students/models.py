from django.db import models

# Create your models here.
class Student (models.Model):
    student_number=models.CharField(max_length=30)
    first_name=models.CharField(max_length=64)
    last_name=models.CharField(max_length=64)
    
