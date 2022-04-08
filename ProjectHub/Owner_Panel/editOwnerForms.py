# from django import forms
from django.forms import ModelForm
from .models import Owner_Panel

class editOwner(ModelForm):
    class Meta:
        model = Owner_Panel
        exclude = ['owner_priority_serial','created']
        #fields = ['name','gmail','number']
        #fields = '__all__'
        
        # widget = {
        #     'featured_image': forms.ImageField
        # }