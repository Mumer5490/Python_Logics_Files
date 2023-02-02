from django.contrib import admin

# Register your models here.
from .models import cat_dog

# Register your models here.
@admin.register(cat_dog)
class bikesAdmin(admin.ModelAdmin):
    list_display = ('name','cat_dog_Img')
