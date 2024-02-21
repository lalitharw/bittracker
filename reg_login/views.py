from django.shortcuts import render,redirect
from .forms import SignUpForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.

#loginForm Function
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = LoginForm(request=request,data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']

                user = authenticate(request,username=uname,password=upass)

                if user is not None:
                    login(request,user)
                    return redirect('home') 
                
            messages.error(request,'Username or Password is incorrect!!')
        
        else:
            fm = LoginForm()
        context = {'form':fm}
        return render(request,'reg_login/login.html',context)
    else:
        return redirect('home')

#signupForm Function
def SignUp(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = SignUpForm(request.POST)
            if fm.is_valid():
                fm.save()
                fm = SignUpForm()
                messages.success(request,'Account create successfully!! Login')
                return redirect('login')
        else:
            fm = SignUpForm()
        context = {'form':fm}
        return render(request,'reg_login/signnew.html',context)
    else:
        return redirect('home')
   
#logout page
def logout_page(request):
    logout(request)
    return redirect('login')


