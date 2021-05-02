from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login, logout
from webapp.models import User_data


def registrationview(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            users = form.save()
            firstname = form.cleaned_data['first_name']
            lastname = form.cleaned_data['last_name']
            username = form.cleaned_data['user_name']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            Newuser = User.objects.create_user(
                first_name=firstname,
                last_name=lastname,
                username=username,
                password=password,
                email=email,)
            Newuser.save()
            return redirect('login_page')

    return render(request, 'registration.html', {'form':form})


def loginview(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        query = User_data.objects.all().filter(email=email)
        if query:
            user_email = query[0].email
            cache.set('my_key', user_email, 10)
            username = query[0].user_name
            user_auth = authenticate(username=username, password=password)
            if user_auth:
                login(request, user_auth)
                return redirect('profile_view')
            else:
                messages.error(request, 'Invalid credentials')
        else :
            messages.error(request, 'Email is not registered')

    return render(request, 'login.html', {})


@login_required(login_url='login_page')
def profileview(request):
    email = cache.get('my_key')
    data = User_data.objects.all().filter(email=email)
    return render(request, 'profile.html', {'data': data})


def user_logout(request):
    logout(request)
    return redirect('login_page')
