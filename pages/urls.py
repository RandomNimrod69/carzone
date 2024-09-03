from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                  # Home page
    path('about/', views.about, name='about'),          # About page
    path('contact/', views.contact, name='contact'),    # Contact page
    path('services/', views.services, name='services'), # Services page
    path('accounts/login/', views.login, name='login'), # Login page
    path('accounts/register/', views.register, name='register'), # Register page
    path('accounts/dashboard/', views.dashboard, name='dashboard'), # Dashboard page
    path('accounts/logout/', views.logout, name='logout'), # Logout page
]
