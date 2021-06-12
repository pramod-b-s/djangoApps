import time

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, HttpResponse, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse


def homepage(request):
    if request.user.is_authenticated:
        return render(request, 'main/homepage.html')
    return HttpResponseRedirect(reverse('main:login'))

def login_request(request):
    if request.user.is_authenticated:
        return render(request, 'main/homepage.html')
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return HttpResponseRedirect(reverse("main:home"))
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request, template_name = "main/login.html", context={"form":form})

@login_required
def logout_request(request):
    prev_user_name = request.user
    logout(request)
    messages.info(request, "Logged out successfully!")
    context={'prev_user_name':prev_user_name}
    return HttpResponseRedirect(reverse("main:home"))


def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return HttpResponseRedirect(reverse("polls:home"))
    context['form']=form
    return render(request,'main/sign_up.html',context)
