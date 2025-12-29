from django.db import models

# Create your models here.

class Magazine(models.Model):
    mno = models.AutoField(primary_key=True)
    mtitle = models.CharField(max_length=1000)
    mcontent = models.TextField()
    mtype = models.CharField(max_length=2)
    mfile = models.FileField(default='',null=True)
    mhit = models.IntegerField(default=0)
    mdate = models.DateTimeField(auto_now=True)
    
    
