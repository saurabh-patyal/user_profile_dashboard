from django.shortcuts import render,redirect
from .forms import SignUpForm,LoginUserForm,ChangePasswordForm,EditUserProfile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import auth
# Create your views here.
#########User Login################
def login(request):
    if request.method == 'POST':
        fm=LoginUserForm(request=request,data=request.POST)
        
        if fm.is_valid():
            username=fm.cleaned_data['username']
            password=fm.cleaned_data['password']
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                messages.success(request,'Login Successfully')
                return redirect('dashboard')
        else:
            fm=LoginUserForm(request=request,data=request.POST)
            context={
                'form':fm,
            }
            return render(request,'accounts/login.html',context)
    fm=LoginUserForm()
    context={
        'form':fm,
    }
    return render(request,'accounts/login.html',context)

##############################User Signp#################
def signup(request):
    if request.method == 'POST':
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            fm.save() 
            messages.success(request,'You are Now Successfully Registered')
            return redirect('login')
            
        else:
            fm=SignUpForm(request.POST)
            context={
                'form':fm,
            }
            return render(request,'accounts/register.html',context)
    
    fm=SignUpForm()
    context={
        'form':fm,
    }
    return render(request,'accounts/register.html',context)



##############Logout user & Redirected to home page#################
@login_required(login_url='login')   
def userlogout(request):
    auth.logout(request)
    messages.success(request,'You are Now Successfully Logged Out')
    return redirect('home')


################change user password from dashboard############
@login_required(login_url='login')
def changeuserpassword(request):
    if request.method =='POST':
        fm=ChangePasswordForm(user=request.user,data=request.POST)
        if fm.is_valid():
            fm.save()        
            messages.success(request,'Your Password Is Changed Successfully')
            return redirect('login')
        else:
            context={
                'form':fm
            }
            fm=ChangePasswordForm(user=request.user,data=request.POST)
            return render(request,'accounts/changepassword.html',context)
    else:
        fm=ChangePasswordForm(user=request.user)
        context={
            'form':fm
        }
        return render(request,'accounts/changepassword.html',context)

################cdit User Profile############
@login_required(login_url='login')
def editProfile(request):
    if request.method =='POST':
       
        fm=EditUserProfile(request.POST,request.FILES,instance=request.user.profile)
        if fm.is_valid():
            fm.save()        
            messages.success(request,'Your Profile Is Successfully Saved')
            return redirect('editProfile')
        else:
            fm=EditUserProfile(request.POST,request.FILES,instance=request.user.profile)
            context={
                'form':fm
            }
            
            return render(request,'accounts/profile.html',context)

    else:
        fm=EditUserProfile(instance=request.user.profile)
        context={
            'form':fm,
            
             }
        return render(request,'accounts/profile.html',context)