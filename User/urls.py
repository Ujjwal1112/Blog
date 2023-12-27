from django.urls import path
import User.views as views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('login', views.user_login, name='login'),
    path('profile', views.user_profile, name='profile'),
    path('edit-profile', views.edit_profile, name='edit_profile'),
    path('register', views.user_register, name='register'),
    path('logout', views.user_logout, name='logout'),
    path('posts', views.public_posts, name='posts')
]
