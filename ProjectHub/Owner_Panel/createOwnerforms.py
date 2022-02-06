from django.forms import ModelForm
from .models import Owner_Panel

class createOwner(ModelForm):
    class Meta:
        model = Owner_Panel
        exclude = ['created']
        #fields = ['name','gmail','number']
        #fields = '__all__'