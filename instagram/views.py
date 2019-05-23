from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile,Post,Following
from .forms import DetailsForm,PostForm

def welcome(request):
    return render(request, 'welcome.html')

@login_required(login_url='/accounts/login/')
def profile(request):
    posts=Post.objects.all()
    current_user = request.user
    if request.method == 'POST':
        form = DetailsForm(request.POST, request.FILES)
        form1 = PostForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()

        if form1.is_valid():
            post = form1.save(commit=False)
            post.profile = current_user.profile
            post.save()

        return redirect('profile')

    else:
        form = DetailsForm()
        form1 = PostForm()
    
    return render(request, 'profile.html', {"form":form,"form1":form1,"posts":posts})

@login_required(login_url='/accounts/login/')
def timeline(request):
    users = User.objects.all()
    posts = Post.objects.all()
    follows = Following.objects.all()
    if request.method=='POST':
        follow_username = request.POST.get("follow")
        follow_user=User.objects.filter(username=follow_username).first()
        following=Following(user=follow_user,followed=request.user.username)
        following.save()
        return redirect('timeline')
    else:
        return render(request, 'timeline.html',{"users":users,"follows":follows,"posts":posts})

@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = DetailsForm(request.POST, request.FILES)
        if form.is_valid():
                Profile.objects.filter(id=current_user.profile.id).update(profile_pic=form.cleaned_data["profile_pic"],bio=form.cleaned_data["bio"])
        return redirect('profile')

    else:
        form = DetailsForm()
    
    return render(request, 'edit_profile.html',{"form": form})
