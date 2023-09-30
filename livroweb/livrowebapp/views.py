from django.shortcuts import render

# Create your views here.
def land(request):
    return render(request, 'livrowebapp/landing.html')
def signin(request):
    return render(request, 'livrowebapp/signin.html')
def signup(request):
    return render(request, 'livrowebapp/signup.html')
def aboutus(request):
    return render(request, 'livrowebapp/aboutus.html')
def readwrite(request):
    return render(request, 'livrowebapp/readwrite.html')