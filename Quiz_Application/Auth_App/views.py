from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from Home_App.models import User
from Auth_App.models import QuesModel, QuesModelTwo
from django.core.paginator import Paginator

# Create your views here.

def profile(request):
    return render(request, 'Auth_App/profile.html')

def authregistration(request):
    if request.method == 'POST':
        registration_username = request.POST['name']
        registration_email = request.POST['email']
        registration_password = request.POST['password']
        registration_confirm_password = request.POST['confirm_password']
        if registration_password == registration_confirm_password:
            
            if User.objects.filter(username=registration_username).exists():
                messages.error(request, 'Username Already Exists')
            elif User.objects.filter(email=registration_email).exists():
                messages.error(request, 'Email Already Exists')
            else:
                registration_user = User.objects.create_user(username=registration_username, password=registration_password, email=registration_email)
                registration_user.save()
                messages.success(request, 'You have Successfully Registered')
                return redirect('login')
        else:
            messages.error(request, 'Password and Conform Password Not Matched')
    
    return render(request, 'Auth_App/registration.html')


def authlogin(request):
    if request.method == 'POST':
        login_email = request.POST['email']
        login_password = request.POST['password']
        auth_user = authenticate(request, email=login_email, password=login_password)
        
        if auth_user is not None:
            login(request, auth_user)
            return redirect('home')
        else:
            messages.error(request, 'Email or Password Invalid !')
        
    return render(request, 'Auth_App/login.html')

def authlogout(request):
    logout(request)
    messages.success(request, 'Logout Successfully')
    return redirect('login')


def home(request):
    if request.method == 'POST':
        print(request.POST)
        questions = QuesModel.objects.all()
        score = 0
        wrong = 0
        correct = 0
        total = 0 
        for q in questions:
            total += 1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans == request.POST.get(q.question):
                score += 10
                correct += 1
            else:
                wrong += 1
                score -= 3
        percent = score/(total*10) *100
        quiz_one_result = {
            'score': score,
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total,
        }
        return render(request,'Auth_App/result.html', context = quiz_one_result)
    
    else:
        questions = QuesModel.objects.all()
        quiz_one_html_questions = {
            'questions': questions
        }
        return render(request,'Auth_App/quiz.html', context = quiz_one_html_questions)

def quiz_two(request):
    if request.method == 'POST':
        quiz_two_questions = QuesModelTwo.objects.all()
        quiz_two_score = 0
        quiz_two_wrong = 0
        quiz_two_correct = 0
        quiz_two_total = 0
        for row in quiz_two_questions:
            quiz_two_total += 1
            if row.ans == request.POST.get(row.question):
                quiz_two_score += 1
                quiz_two_correct += 0.33
            else:
                quiz_two_wrong += 1
                quiz_two_score -= 3
        quiz_two_percent = (quiz_two_score/(quiz_two_total)) * 100
        quiz_two_result = {
            'score': quiz_two_score,
            'correct': quiz_two_correct,
            'wrong': quiz_two_wrong,
            'percent': quiz_two_percent,
            'total': quiz_two_total,
        }
        return render(request,'Auth_App/result_two.html', context = quiz_two_result)
    
    else:
        quiz_two_questions = QuesModelTwo.objects.all()
        quiz_two_html_questions = {
            'questions': quiz_two_questions
        }
        return render(request,'Auth_App/quiz_two.html', context = quiz_two_html_questions)

                