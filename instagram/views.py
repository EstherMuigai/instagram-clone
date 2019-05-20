from django.shortcuts import render
from django.http  import HttpResponse

def welcome(request):
    return render(request, 'welcome.html')

def profile(request):
    return render(request, 'profile.html')

def timeline(request):
    return render(request, 'timeline.html')
