from getpass import getuser
from django.urls import path 
from django.contrib.auth import views as auth_views

from . import views 


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/done', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('account/profile/', views.account_profile, name='account_profile'),    
    path('users/<int:uid>/', views.user_home, name='user_home'), 
    path('users/<int:uid>/idea', views.an_idea, name='an_idea'), 
    path('users/<int:uid>/idea/<int:idea_id>/', views.my_idea, name='my_ideas'), 
]