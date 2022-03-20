from django.shortcuts import render


def index(request):
    return render(request, 'users/login.html')


def signup(request):
    if request.method == 'POST':
        pass
    return render(request, 'users/signup.html')
