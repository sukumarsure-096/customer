from django.db import models

# Create your models here.
class category(models.Model):
    catid = models.CharField(max_length=10,primary_key=True,unique=True)
    age = models.IntegerField()

    def __str__(self):
        return self.catid

class flipkart(models.Model):
    fid = models.CharField(max_length=10,primary_key=True,unique=True)
    fname = models.CharField(max_length=30)
    fprice = models.IntegerField()
    catid = models.ForeignKey(category,on_delete=models.CASCADE)

    def __str__(self):
        return self.fid
    
class amazon(models.Model):
    aid = models.CharField(max_length=10,primary_key=True,unique=True)
    aname = models.CharField(max_length=30)
    aprice = models.IntegerField()
    catid = models.ForeignKey(category,on_delete=models.CASCADE)

    def __str__(self):
        return self.aid
        

class customer(models.Model):
    cid = models.CharField(max_length=10,primary_key=True,unique=True)
    cname = models.CharField(max_length=30)
    cmobile = models.CharField(max_length=10)
    caddress = models.CharField(max_length=50)
    fid = models.ForeignKey(flipkart,on_delete=models.CASCADE)
    aid = models.ForeignKey(amazon,on_delete=models.CASCADE)
    
