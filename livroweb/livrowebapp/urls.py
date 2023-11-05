from django.urls import path
from . import views

urlpatterns = [
    path('', views.land),
    path('signin/', views.signin),
    path('signup/', views.signup),
    path('aboutus/', views.aboutus),
    path('readwrite/', views.readwrite),
    path('profile/', views.profile),
    path('home/', views.home),
    path('addbooks/', views.addbooks),
    path('browse/', views.browse),
    path('manageprofile/', views.manageprofile),
    path('profile_writer/', views.profile_writer),
    path('bookinformation/', views.bookinformation),
    path('browse_reader/', views.browse_reader),
    path('browse_writer/', views.browse_writer),
]
