from django.shortcuts import render

# Create your views here.
def land(request):
    return render(request, 'livrowebapp/landing.html')
def signin(request):
    return render(request, 'livrowebapp/signin.html')