from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.main, name= 'main'),
    path('signup/',views.signup, name= 'signup'),
    path('forgetPs/', views.forgetPs, name='forgetPs'),
    path('editprofile/', views.editprofile, name='editprofile'),
    path('logout/', views.logout, name='logout'),
]