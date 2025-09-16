from django.db import models

# Create your models here.
class Attend(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=3)
    is_present = models.BooleanField()
    date = models.DateField()

