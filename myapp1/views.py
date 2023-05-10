from django.shortcuts import render

# Create your views here.

def RegistrForm_page(request):
    return render(request, 'RegistrForm.html')

def about_page(request):
    return render(request, 'about.html')
