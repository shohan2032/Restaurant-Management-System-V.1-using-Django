from email.policy import default
from django.db import models
import uuid

# Create your models here.
class Owner_Panel(models.Model):
    featured_image = models.ImageField(blank=True,null=True,default='default.jpg')
    name = models.CharField(max_length=200, null=False, blank=False)
    gmail = models.CharField(max_length=200, null=False, blank=False)
    number = models.IntegerField(null=False, blank=False)
    ownership = models.CharField(max_length=200, null=False, blank=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    owner_priority_serial = models.IntegerField(null=True, blank=True)
    Facebook_URL = models.CharField(max_length=200, null=True, blank=True)
    Linkedin_URL = models.CharField(max_length=200, null=True, blank=True)
    Instagram_URL = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return self.name + ' - ' + str(self.owner_priority_serial)



class Food_Panel(models.Model):
    featured_image = models.ImageField(blank=True,null=True,default='default.jpg')
    name = models.CharField(max_length=200, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    food_priority_serial = models.IntegerField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name + ' - ' + str(self.food_priority_serial)