from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def authlogin(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('profile')
        else:
            print ('Invalid')   



    return render(request,'authentication/login.html')

def authlogout(request):
    
    logout(request)


    return redirect('login')  

def authregistration(request):

     if request.method== 'POST':
      username = request.POST['name']
      email = request.POST['email']
      password = request.POST['password']
      confirmpassword = request.POST['Confirm password']

      if(password==confirmpassword):
        print('adsf')

      else:
        print('error')  
    
     return render(request,'authentication/registration.html')

def forgot(request):
    return render(request,'authentication/forget.html')        
