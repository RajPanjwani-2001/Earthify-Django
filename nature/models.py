from django.db import models
from datetime import date

# Create your models here.
class Projects(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to = 'pics')
    desc = models.TextField()
    date = models.DateField(default=date.today())
    hlink = models.URLField(max_length=200)
 