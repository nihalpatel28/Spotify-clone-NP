from django.db import models

# Create your models here.


class Subject(models.Model):
    subject_name = models.CharField(max_length=256 ,blank=False)
    description = models.TextField(max_length=1000,blank=True)




class Youtube(models.Model):
    link  = models.URLField(max_length=1000,blank=True,null=True)
    