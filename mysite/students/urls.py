from django.urls import include, path
from . import views

urlpatterns = [
    path('homepage/', views.homepage, name= 'homepage'),
    path('about/', views.about, name= 'about'),
    path('contact/', views.contact, name= 'contact'),


]
