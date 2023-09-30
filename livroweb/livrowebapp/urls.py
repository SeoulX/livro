from django.urls import path
from . import views

urlpatterns = [
    path('', views.land),
    path('signin/', views.signin),
    path('signup/', views.signup),
    path('aboutus/', views.aboutus),
    path('readwrite/', views.readwrite),
]