from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# from cat_dog_app import views
from . import views



urlpatterns = [
    
    
    path('', views.show_index,name="index"),
    path('abc', views.catdog,name="success"), # this line is must with ulr link like abc
    

]

# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)