from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import DetailsForm

def welcome(request):
    return render(request, 'welcome.html')

#@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request, 'profile.html')

@login_required(login_url='/accounts/login/')
def timeline(request):
    return render(request, 'timeline.html')

@login_required(login_url='/accounts/login/')
def edit_profile(request):
    profiles=Profile.objects.all()
    current_user = request.user
    if request.method == 'POST':
        form = DetailsForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('profile')

    else:
        form = DetailsForm()
    
    return render(request, 'edit_profile.html',{"form": form, "profiles":profiles})
