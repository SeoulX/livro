from django.db import models

class Member(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    type_user = models.CharField(max_length=10)
    
    def __str__(self):
        return self.username
    
