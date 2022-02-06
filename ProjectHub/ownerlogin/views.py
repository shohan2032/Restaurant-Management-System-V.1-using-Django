from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def ownerlogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Owner_list')
        else:
            messages.error(request,"Wrong Credentials, Try Again")
            return redirect('ownerlogin')
    return render(request, 'ownerlogin/login.html', {})