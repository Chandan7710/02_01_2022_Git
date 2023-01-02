from django.urls import path
from Auth_App import views

urlpatterns = [
    
    path('profile/', views.profile, name = 'profile'),
    path('login', views.authlogin, name = 'login'),
    path('registration/', views.authregistration, name = 'registration'),
    path('logout/', views.authlogout, name = 'logout'),
    path('quiz/', views.home, name='home'),
    path('quiz_two/', views.quiz_two, name='quiz_two'),

]