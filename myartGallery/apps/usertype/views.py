from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import SignUpForm, LoginForm


# Create your views here.
def register(request):
    msg = ''

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
        else:
            msg = 'form is not valid'

    else:
        form = SignUpForm()

    return render(request, 'registration/register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print('userType:', user.userType)
            if user:
                login(request, user)

                if user.userType == 'Artist':
                    return redirect('home')  # Redirect to the artist's home page
                elif user.userType == 'Citizen':
                    return redirect('welcome')  # Redirect to the citizen's welcome page

        else:
            msg = 'Invalid username or password. Please try again.'
    return render(request, 'registration/login.html', {'form': form, 'msg': msg})


def logout_view(request):
    logout(request)
    return redirect('/login')
