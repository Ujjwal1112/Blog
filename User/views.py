from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from User.models import Profile, UserBlog
from User.helper import generate_url

DEFAULT_PIC = "https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava1-bg.webp"
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
            return redirect('profile')           
            
        else:
            error_message = "INVALID EMAIL OR PASSWORD"
            messages.info(request, error_message)
            print(valid_user)
            return redirect('login')
                  
    return render(request, 'login.html')

@login_required
def user_profile(request):
    profile = Profile.objects.get(user_id=request.user.pk)
    if not profile.profile_pic:
        profile.profile_pic = DEFAULT_PIC
        profile.save()
    context = {'profile': profile}
    return render(request, 'profile.html', context)


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

@login_required
def user_logout(request):
    user=User.objects.get(id=request.user.pk)
    logout(request)
    return redirect('home')

@login_required
def edit_profile(request):
    profile = Profile.objects.get(user_id=request.user.pk)
    context = {'profile': profile}
    if request.method=='POST':
        phone_num =  request.POST.get('phone_num')
        address = request.POST.get('address')
        profile_pic = request.FILES.get('profile_pic')
        profile.phone_num = phone_num
        profile.address = address
        
        print(phone_num, address, profile_pic)
        
        if profile_pic:
            url = generate_url(request, profile_pic)
            print('HELLO')
            profile.profile_pic = url
            
        profile.save()
        print('AKSDFASL')
        return redirect('edit_profile')
        
    return render(request, 'edit-profile.html', context)


def public_posts(request):
    return render(request, 'posts.html')



def create_post(request):    
    context = {"bog":"dd"}
    
    if request.method == 'POST':
        title = request.POST.get("title")
        body = request.POST.get("body")
        UserBlog.objects.create(user_id=request.user.id, title=title, body=body)
        return redirect('home')
        
    return render(request, template_name="create-post.html", context=context)


def my_post(request):
    posts = UserBlog.objects.filter(user_id=request.user.pk)
    context = {"posts": posts}
    return render(request, "my-post.html", context)