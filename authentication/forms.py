from django.forms import ModelForm
from .models import Items
class ItemsForm(ModelForm):
    
    class Meta:
        model = Items
        fields = '__all__'
