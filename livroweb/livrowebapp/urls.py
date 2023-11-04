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
    path('bookinformation/', views.bookinformation),

]