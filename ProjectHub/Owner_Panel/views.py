from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Owner_Panel,Food_Panel
from .createOwnerforms import createOwner
from .editOwnerForms import editOwner
from .editFoodForms import editFood
from .createFoodForms import addFood
from .utils import searchOwners,searchfoods
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


##Showing all owner in a page with this fucntion
def Owner_list(request):
    owners, search_owner = searchOwners(request)
    context = {'owners':owners,
               'search_owner':search_owner}
    # all_owner_list = Owner_Panel.objects.all()
    # context = {'ownerlist':all_owner_list}
    return render(request, 'Owner_Panel/Owner_List.html',context=context)


##Showing all details of an owner with this function 
def Owner_details(request,owner_id):
    perticular_owner_details = Owner_Panel.objects.get(id=owner_id)
    context = {'particular_owner':perticular_owner_details}
    return render(request, 'Owner_Panel/Owner_details.html',context=context)


##Adding new owner to owner list with this function
def create_owner(request):
    form = createOwner()
    context = {'form':form}
    if request.method == 'POST':
        form = createOwner(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Owner_list')
        else:
            return HttpResponse('<h1>Owner not Created</h1>')
        
    #it will come here when request.method == "GET"
    return render(request,'Owner_Panel/create_owner.html', context)


##Editing owner information with this function
def edit_owner(request,owner_id):
    perticular_owner_details = Owner_Panel.objects.get(id=owner_id)
    form = editOwner(instance=perticular_owner_details)
    context = {'form':form,'perticular_owner':perticular_owner_details}
    if request.method == 'POST':
        form = editOwner(request.POST, request.FILES, instance=perticular_owner_details)
        if form.is_valid():
            form.save()
            return redirect('Owner_details',owner_id)
    return render(request,'Owner_Panel/edit_owner.html', context)


##Deleting an owner from the owner list with this function
def delete_owner(request,owner_id):
    perticular_owner_details = Owner_Panel.objects.get(id=owner_id)
    if request.method == 'POST':
        perticular_owner_details.delete()
        return redirect('Owner_list')
    context = {'perticular_owner':perticular_owner_details}
    return render(request,'Owner_Panel/delete_owner.html', context)


##owner login function for login into the ownerpanel page
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
    return render(request, 'Owner_Panel/login.html', {})


##logout function for an owner
def owner_logout(request):
    logout(request)
    messages.success(request,"Successfully logged out")
    return redirect('ownerlogin')


##Showing all food menu in a page with this fucntion
def food_list(request):
    foods, search_food = searchfoods(request)
    context = {'foods':foods,
               'search_food':search_food}
    return render(request, 'Owner_Panel/food_List.html',context=context)


##Showing all details of a food with this function 
def food_details(request,food_id):
    perticular_food_details = Food_Panel.objects.get(id=food_id)
    context = {'particular_food':perticular_food_details}
    return render(request, 'Owner_Panel/food_details.html',context=context)


##editting a particular food menu with this function
def edit_food(request,food_id):
    perticular_food_details = Food_Panel.objects.get(id=food_id)
    form = editFood(instance=perticular_food_details)
    context = {'form':form,'perticular_food':perticular_food_details}
    if request.method == 'POST':
        form = editFood(request.POST, request.FILES, instance=perticular_food_details)
        if form.is_valid():
            form.save()
            return redirect('food_details',food_id)
    return render(request,'Owner_Panel/edit_food.html', context)


##deleting a food menu from the food list with this funtion
def delete_food(request,food_id):
    perticular_food_details = Food_Panel.objects.get(id=food_id)
    if request.method == 'POST':
        perticular_food_details.delete()
        return redirect('food_list')
    context = {'perticular_food':perticular_food_details}
    return render(request,'Owner_Panel/delete_food.html', context)


##Adding new food menu to the food list with this function
def add_food(request):
    form = addFood()
    context = {'form':form}
    if request.method == 'POST':
        form = addFood(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('food_list')
        else:
            return HttpResponse('<h1>Food not Created</h1>')
        
    #it will come here when request.method == "GET"
    return render(request,'Owner_Panel/create_food.html', context)