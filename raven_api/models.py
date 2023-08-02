from django.db import models
from django.contrib.auth.models import User
# Create your models here.
 
class Project(models.Model):
    name  = models.CharField(max_length = 20, null = False) 
    description = models.TextField(max_length = 120, null =False)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length = 20 , default = "pending",null = False)
    Owner = models.ForeignKey(User,on_delete = models.CASCADE, related_name = "Client")

    def  __str__ (self): 
        return f' {self.id} --  {self.name}'
