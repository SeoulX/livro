from django.shortcuts import render

# Create your views here.
def land(request):
    return render(request, 'livrowebapp/addbooks.html')
def signin(request):
    return render(request, 'livrowebapp/signin.html')
def signup(request):
    return render(request, 'livrowebapp/signup.html')
def aboutus(request):
    return render(request, 'livrowebapp/aboutus.html')
def readwrite(request):
    return render(request, 'livrowebapp/readwrite.html')
def profile(request):
    return render(request, 'livrowebapp/profile.html')