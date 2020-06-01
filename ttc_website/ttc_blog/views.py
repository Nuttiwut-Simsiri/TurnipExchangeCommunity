from django.shortcuts import render



def render_index(request):
    return render(request, 'index.html', {"page_title": "==== Turnip Trader Community ===="})

def render_login(request):
    return render(request, 'login.html', {"page_title": "==== Login ===="})

def render_sign_up(request):
    return render(request, 'sign-up.html', {"page_title": "==== Sign up to our community ===="})

def render_webboard(request):
    pass
