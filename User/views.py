from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from User.models import Profile

# Create your views here.
def home_page(request):
    return render(request, 'home.html')

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(email=email)
        if not user.exists():
            error_message = "EMAIL DOES NOT EXISTS"
            messages.error(request, error_message)
            return redirect('login')
        username=user[0].username
        valid_user = authenticate(username=username, password=password)
        if valid_user:
            error_message = "YOU ARE LOGGED IN"
            messages.info(request, error_message)
            login(request, valid_user)
            print(valid_user)
            return redirect('profile')           
            
        else:
            error_message = "INVALID EMAIL OR PASSWORD"
            messages.info(request, error_message)
            print(valid_user)
            return redirect('login')
                  
    return render(request, 'login.html')

def user_profile(request):
    return render(request, 'profile.html')


def user_register(request):
    if request.method =="POST":
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get("email")
        password = request.POST.get("password")
        re_password = request.POST.get("re_password")
        phone_num = request.POST.get("phone_num")
        address = request.POST.get("address")
        if password != re_password:
            error_message = 'PASSWORD IS NOT SAME'
            messages.error(request, error_message)
            return redirect('register')
        valid_user = User.objects.filter(email=email)
        if valid_user.exists():
            error_message = 'EMAIL ALRAEDY EXISTS'
            messages.error(request, error_message)
            return redirect('register')        
        if User.objects.filter(username=username).exists():
            error_message = 'USERNAME ALREADY EXISTS'
            messages.error(request, error_message)
            return redirect('register')            
        if not valid_user.exists():
            user = User(username=username, email=email, first_name=name)
            user.set_password(password)
            user.save()
            profile = Profile(user=user, phone_num=phone_num, address=address )
            profile.save()
            return redirect('login')
    return render(request, 'register.html')
