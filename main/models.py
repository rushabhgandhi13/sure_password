from django.db import models

# Create your models here.
class User(models.Model):   
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email= models.CharField(max_length=100)
    master_password= models.CharField(max_length=500)
    key= models.CharField(max_length=500)
    
    def __str__(self):
        return str(self.id)+" "+self.name

class Service(models.Model):   
    service_name = models.CharField(max_length=50)
    user = models.ForeignKey(User, default=0, on_delete=models.CASCADE)
    password= models.CharField(max_length=100)
    
    def __str__(self):
        return self.service_name

        
