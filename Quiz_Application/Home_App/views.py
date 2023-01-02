from django.shortcuts import render
from Auth_App.models import contactform

# Create your views here.

def home(request):
    return render(request, 'Home_App/home.html')

def about(request):
    return render(request, 'Home_App/about.html')

def contact(request):
    if request.method == 'POST':
        contact_name = request.POST.get('name')
        contact_email = request.POST.get('email')
        contact_subject = request.POST.get('subject')
        contact_message = request.POST.get('message')
        
        contactformdata = contactform(name=contact_name, email=contact_email, subject=contact_subject, message=contact_message)
        contactformdata.save()
    
    return render(request, 'Home_App/contact.html')

