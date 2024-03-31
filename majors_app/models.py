from django.db import models

# Create your models here.

class Majors(models.Model):

    major_name = models.CharField(max_length=30, null=False)
    image = models.ImageField(upload_to='major/', null=True, blank=True, default='')

    def __str__(self):
        return self.major_name
