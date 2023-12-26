from django.urls import path
import User.views as views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('login', views.user_login, name='login'),
    path('profile', views.user_profile, name='profile'),
    path('register', views.user_register, name='register')
]
