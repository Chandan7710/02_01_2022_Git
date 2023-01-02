from django.urls import path
from Home_App import views

urlpatterns = [
    
    path('', views.home, name = 'home1'),
    path('about/', views.about, name = 'about'),
    path('contact/', views.contact, name = 'contact'),
    
]