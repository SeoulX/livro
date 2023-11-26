from django.urls import path
from . import views

urlpatterns = [
    path('', views.land, name='land'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('profile/', views.profile, name='profile'),
    path('home/', views.home, name='home'),
    path('addbooks/', views.addbooks, name='addbooks'),
    path('browse/', views.browse, name='browse'),
    path('manageprofile/', views.manageprofile, name='manageprofile'),
    path('manageprofile_writer/', views.manageprofile_writer, name='manageprofile_writer'),
    path('profile_writer/', views.profile_writer, name='profile_writer'),
    path('bookinformation/', views.bookinformation, name='bookinformation'),
    path('browse_reader/', views.browse_reader, name='browse_reader'),
    path('browse_writer/', views.browse_writer, name='browse_writer'),
]
