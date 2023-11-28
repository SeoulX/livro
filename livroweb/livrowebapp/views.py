from datetime import datetime
from django.shortcuts import render, redirect
from .models import Member
from .forms import Memberform
from django.contrib import messages

def land(request):
    return render(request, 'livrowebapp/landing.html')
def signin(request):
    if request.method == "GET":
        mail = request.GET.get('mail')
        passw = request.GET.get('pass')
        now = datetime.now()
        hour = now.hour
        greeting = 'Good Morning' if 5 <= hour < 12 else ('Good afternoon' if 12 <= hour < 18 else 'Good Evening')
        try:
            member = Member.objects.get(email=mail, password=passw)
            if member.type_user == 'Reader':
                messages.success(request, f'{greeting}, {member.username}!')
                return redirect('browse_reader')
            elif member.type_user == 'Writer':
                messages.success(request, f'{greeting}, {member.username}!')
                return redirect('browse_writer')
        except Member.DoesNotExist:
            return render(request, 'livrowebapp/signin.html')
    else:
        return render(request, 'livrowebapp/signin.html')
def signup(request):
    if request.method == "POST":
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
        return render(request, 'livrowebapp/signup.html')
def aboutus(request):
    return render(request, 'livrowebapp/aboutus.html')
def readwrite(request):
    return render(request, 'livrowebapp/readwrite.html')
def profile(request):
    return render(request, 'livrowebapp/profile.html')
def home(request):
    return render(request, 'livrowebapp/home.html')
def addbooks(request):
    return render(request, 'livrowebapp/addbooks.html')
def browse(request):
    return render(request, 'livrowebapp/browse.html')
def manageprofile(request):
    return render(request, 'livrowebapp/manageprofile.html')
def manageprofile_writer(request):
    return render(request, 'livrowebapp/manageprofile_writer.html')
def profile_writer(request):
    return render(request, 'livrowebapp/profile_writer.html')
def bookinformation(request):
    return render(request, 'livrowebapp/bookinformation.html')
def browse_reader(request):
    return render(request, 'livrowebapp/browse_reader.html')
def browse_writer(request):
    return render(request, 'livrowebapp/browse_writer.html')