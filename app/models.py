from django.db import models

# Create your models here.

class Bank(models.Model):
    bname = models.CharField(max_length=100)
    

    def __str__(self):
        return self.bname

class Branch(models.Model):
    bname = models.ForeignKey(Bank,on_delete=models.CASCADE)
    ifcs = models.CharField(max_length = 150,primary_key=True)
    branch = models.CharField(max_length = 150)
    address = models.CharField(max_length = 150)
    contract = models.IntegerField()
    city = models.CharField(max_length = 150)
    district = models.CharField(max_length = 150)
    state = models.CharField(max_length = 150)
    
    
    
    
    
       
    

    def __str__(self):
        return self.branch