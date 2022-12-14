from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=170)
    password = models.CharField(max_length=16)

    
# if student is registered only then add student to course else throw error
class Course(models.Model):
    name_course = models.CharField(max_length=70)
    email_course = models.EmailField(max_length=170)
    password_course = models.CharField(max_length=16)







