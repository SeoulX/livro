from django.db import models

class Member(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=16)
    type_user = models.CharField(max_length=10)
    active = models.BooleanField(default=True) 
    
    def __str__(self):
        return self.username
    
