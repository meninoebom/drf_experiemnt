from django.db import models

# Create your models here.

class Resume(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, null=True, blank=True)
    github = models.URLField(max_length=200)
    qualifications = models.ManyToManyField('Qualification', related_name='resume')

class Qualification(models.Model):
    name = models.CharField(max_length=50)

class Experience(models.Model):
    job_title = models.CharField(max_length=100)
    duties = models.CharField(max_length=1000)
    resume = models.ForeignKey('Resume')