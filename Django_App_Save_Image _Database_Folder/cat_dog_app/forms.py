from django import forms
from .models import cat_dog
  
class CatForm(forms.ModelForm):
  
    class Meta:
        model = cat_dog
        fields = ['name', 'cat_dog_Img']