from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return render(request, 'students/index.html')

def about(request):
    return render(request, 'students/about.html')

def contact(request):
    return render(request, 'students/contact.html')
