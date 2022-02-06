from django.forms import ModelForm
from .models import Food_Panel

class addFood(ModelForm):
    class Meta:
        model = Food_Panel
        exclude = ['created']
        #fields = ['name','gmail','number']
        #fields = '__all__'