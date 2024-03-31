from django.db import models
from majors_app.models import Majors



class Subjects(models.Model):
    major = models.ForeignKey(Majors, on_delete=models.SET_NULL, related_name='subject', null=True)

    year = models.CharField(max_length=20, null=True, blank=True, default='')
    semester = models.CharField(max_length=20, null=True, blank=True, default='')
    prof_name = models.CharField(max_length=20, null=True, blank=True, default='')
    subject_name = models.CharField(max_length=30, null=True, blank=True, default='')
    midterm = models.FileField(upload_to='midterm/', null=True, blank=True, default='')
    final_exam = models.FileField(upload_to='final_exam/', null=True, blank=True, default='')


    def __str__(self):
        return self.subject_name

