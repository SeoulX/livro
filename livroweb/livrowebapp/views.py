from datetime import datetime
from django.shortcuts import render, redirect
from .models import *
from .forms import Memberform
from django.contrib import messages
from django.db.models import Q

def land(request):
    return render(request, 'livrowebapp/landing.html')
def signin(request):
    if request.method == "GET":
        identifier = request.GET.get('identifier')
        passw = request.GET.get('pass')
        now = datetime.now()
        hour = now.hour
        greeting = 'Good Morning' if 5 <= hour < 12 else ('Good afternoon' if 12 <= hour < 18 else 'Good Evening')
        try:
            member = Member.objects.get(Q(email=identifier) | Q(username=identifier), password=passw)
            request.session['member'] = {
                    'username': member.username,
                    'email': member.email,
                    'password' : member.password,
                    'type_user': member.type_user,
                    'about_user': member.about_user
                }
            if member.type_user == 'Reader':
                messages.success(request, f'{greeting}, {member.username}!')
                return redirect('browse_reader')
            elif member.type_user == 'Writer':
                messages.success(request, f'{greeting}, {member.username}!')
                return redirect('browse_writer')
        except Member.DoesNotExist as e:
            print(f"Error: {e}")
            return render(request, 'livrowebapp/signin.html')
    else:
        return render(request, 'livrowebapp/signin.html')
def signup(request):
    if request.method == "POST":
        passw = request.POST.get('passw')
        confirmpass = request.POST.get('confirmpass')
        if(passw == confirmpass):
            form = Memberform(request.POST or None)
            if form.is_valid():
                member = form.save()
                if member.type_user == 'Reader':
                    messages.success(request, ('Thanks for Signing Up!'))
                    return redirect('browse_reader')
                elif member.type_user == 'Writer':
                    messages.success(request, ('Thanks for Signing Up!'))
                    return redirect('browse_writer')
        else:
            messages.error(request, ('Password Not Match!'))
    else:    
        return render(request, 'livrowebapp/signup.html')
def aboutus(request):
    return render(request, 'livrowebapp/aboutus.html')
def aboutus_logged(request):
    member_data = request.session.get('member', None)
    return render(request, 'livrowebapp/aboutus_logged.html', {'member': member_data})
def browse_reader(request):
    member_data = request.session.get('member', None)
    return render(request, 'livrowebapp/browse_reader.html', {'member': member_data})
def browse_writer(request):
    member_data = request.session.get('member', None)
    return render(request, 'livrowebapp/browse_writer.html', {'member': member_data})
def profile(request):
    member_data = request.session.get('member', None)
    return render(request, 'livrowebapp/profile.html', {'member': member_data})
def profile_writer(request):
    member_data = request.session.get('member', None)
    return render(request, 'livrowebapp/profile_writer.html', {'member': member_data})
def manageprofile(request):
    member_data = request.session.get('member', None)
    return render(request, 'livrowebapp/manageprofile.html', {'member': member_data})
def manageprofile_writer(request):
    member_data = request.session.get('member', None)
    return render(request, 'livrowebapp/manageprofile_writer.html', {'member': member_data})
def addbooks(request):
    member_data = request.session.get('member', None)
    return render(request, 'livrowebapp/addbooks.html')
def home(request):
    return render(request, 'livrowebapp/home.html')
def browse(request):
    return render(request, 'livrowebapp/browse.html')
def bookinformation(request):
    return render(request, 'livrowebapp/bookinformation.html')
def fantasy(request):
    return render(request, 'livrowebapp/books/fantasy.html')
def action(request):
    return render(request, 'livrowebapp/books/action.html')
def updatebooks(request):
    return render(request, 'livrowebapp/updatebooks.html')