from django.shortcuts import render, redirect
from django.contrib import messages
from ttc_blog.forms import SignUpForm, LoginForm
from django.contrib.auth import login, logout, authenticate
import requests
import sys

def render_index(request):
    return render(request, 'index.html', {"page_title": "==== Turnip Trader Community ===="})

def render_login(request):
    if request.method == "GET":
        return render(request, 'login.html', {"page_title": "==== Login ===="})

    elif request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Welcome new member to our community')
            return redirect('/ttc/webboard')
        
        messages.success(request, "We not found your acccount in our community.")
        return render(request, 'login.html', {"page_title": "==== Login ===="})


def render_sign_up(request):
    if request.method == "GET":
        return render(request, 'sign-up.html', {"page_title": "==== Sign up to our community ===="})
        
    elif request.method == "POST":
        sign_up_form = SignUpForm(request.POST)
        if sign_up_form.is_valid():
            sign_up_data = {
                'username': sign_up_form.cleaned_data.get('username'),
                'first_name': sign_up_form.cleaned_data.get('firstname'),
                'last_name': sign_up_form.cleaned_data.get('lastname'),
                'password': sign_up_form.cleaned_data.get('password'),
                'email': sign_up_form.cleaned_data.get('email'),
            }
            response = requests.post('http://127.0.0.1:8000/ttc-api/users', json=sign_up_data)

            if response.status_code == requests.codes.created:
                messages.success(request, 'Welcome new member to our community, please log in to join the community')
                return render(request, 'index.html', {"page_title": "==== Turnip Trader Community ===="})
            else:
                messages.success(request, response.content)
                return render(request, 'sign-up.html', {"page_title": "==== Sign up to our community ===="})
    
        messages.success(request, "Sign up Form invalid !")
        return render(request, 'sign-up.html', {"page_title": "==== Sign up to our community ===="})


def render_webboard(request):
    if request.method == "GET":
        return render(request, 'webboard.html', {"page_title": "==== Sign up to our community ===="})

    elif requests.mothod == "POST":
        pass 


def logout(request):
    logout(request)
    return redirect('/ttc/webboard/welcome')