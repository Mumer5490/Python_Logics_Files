from django.shortcuts import render
from django.http import HttpResponse
from .forms import *

# Create your views here.

def show_index(request):
    
    return render(request, 'index.html')

# def load(request):
    
#     return render(request, 'load.html')

def catdog(request):
    if request.method == 'POST':

        form = CatForm(request.POST, request.FILES)
                
        form.save()
        return HttpResponse('data uploaded')
    else:
        return HttpResponse('not upload image')
  
# def success(request):
#     return HttpResponse('successfully uploaded')

