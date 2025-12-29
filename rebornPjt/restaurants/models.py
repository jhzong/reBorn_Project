from django.db import models

class Restaurants(models.Model):
    resno=models.IntegerField(primary_key=True)
    locno=models.IntegerField(default=0)
    res_name=models.CharField(max_length=50)
    desc=models.TextField(null=True)
    addr=models.CharField(max_length=200)
    tel=models.CharField(max_length=13)
    lat=models.DecimalField(max_digits=10,decimal_places=7)
    lng=models.DecimalField(max_digits=10,decimal_places=7)
    date=models.DateTimeField(auto_now=True)
    mem_id=models.CharField(max_length=25)
    
    def __str__(self):
        return f"{self.resno},{self.res_name},{self.tel},{self.mem_id}"