from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.authlogin, name='login'),
    path('registration/', views.authregistration, name='registration'),
    path('forgotpassword/', views.forgot, name='forgotpassword'),
     path('logout/', views.authlogout, name='logout')
]
