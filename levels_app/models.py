from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Level(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='level')
    your_id = models.CharField(max_length=30, unique=True, null=False, blank=False, default='')
    your_file = models.FileField(upload_to='level_files/', null=False, blank=False, default='')

    def __str__(self):
        return f'{self.pk} : {self.your_id}'

