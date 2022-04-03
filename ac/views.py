from contextlib import redirect_stderr
import email
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def ulogin(request):
    if request.method == 'POST':
        uusername=request.POST['name']
        upassword=request.POST['mobile']
        user = authenticate(request, username=uusername, password=upassword)
        if user is not None:
            login(request, user)
            messages.warning(request,'Login Sucessfully!')
            return redirect('home')
        else:
            messages.warning(request,'Invalid Entry,Try Again!')
            return render(request,'login.html')
    else:
        return render(request,'login.html')    

def ulogout(request):
    logout(request)
    messages.warning(request,'Logout Succesfully')
    return  redirect ('home')