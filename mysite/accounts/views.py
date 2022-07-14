from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User

def main(request):
    if request.method == "GET":
        return render(request, 'accounts/main.html')

    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
                login(request, user)
                # Redirect to a success page.
                return HttpResponseRedirect(reverse('chat:index'))
        else:
            # Return an 'invalid login' error message.
            return render(request, 'accounts/main.html', {'error':'아이디/비밀번호가 잘못되었습니다.'})

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password1'],
            email=request.POST['email'],)
            auth.login(request, user)
            return redirect('/')
        return render(request, 'accounts/signup.html')
    return render(request, 'accounts/signup.html')

def logout(request):
    auth.logout(request)
    return redirect('accounts/main.html')



def editprofile(request):
    return render(request, 'accounts/editProfile.html')

def forgetPs(request):
    return render(request, 'accounts/forgetPs.html')