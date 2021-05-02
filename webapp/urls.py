from django.urls import path
from . import views

urlpatterns = [
    path('', views.registrationview, name="registration_view"),
    path('login/', views.loginview, name='login_page'),
    path('profile/', views.profileview, name='profile_view'),
    path('logout/', views.user_logout, name='logged_out'),

]
