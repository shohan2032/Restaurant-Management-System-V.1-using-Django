from django.forms import ModelForm
from .models import Food_Panel

class editFood(ModelForm):
    class Meta:
        model = Food_Panel
        exclude = ['food_priority_serial','created']
        #fields = ['name','gmail','number']
        #fields = '__all__'