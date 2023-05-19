from django.shortcuts import render,redirect
from vehicles.models import *
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import permission_required
# Create your views here.

def index(request):
    return render(request,"index.html")

def register(request):  
    if request.method == 'POST':
        form = UserForm(request.POST)  
        if form.is_valid():
            username = request.POST.get("username")
            role = request.POST.get("access")
            form.save()
            uid = User.objects.get(username=username)
            if role=='admin':
                uid.user_permissions.add(26,28)
                # my_group = Group.objects.get(name='admin')
            else:
                uid.user_permissions.add(28)
                # my_group = Group.objects.get(name='user') 
            # my_group.user_set.add(uid)
            messages.success(request, 'Account created successfully')  
            return redirect('/')
    else:  
        form = UserForm()  
    context = {  
        'form':form  
    }  
    return render(request, 'register.html', context)  

def loginn(request):
    if request.POST:
        uname = request.POST.get("username")
        upass = request.POST.get("password")
        user = authenticate(request,username=uname,password=upass)
        if user is not None:
            request.session["uid"]=user.id
            login(request,user)
            return redirect("/")
        else:
            messages.error(request,"Incorrect credentials.")
            return render(request,"login.html")
    else:
        return render(request,"login.html")
    
def logoutt(request):
    logout(request)
    return redirect("/")

@permission_required('vehicles.view_vehicle')
def retrieve(request):
    data = Vehicle.objects.all()
    context = { 'vlist':data }
    return render(request,'retrieve.html',context)

@permission_required('vehicles.add_vehicle')
def create(request):
    if request.method == "POST":
        f = VehicleForm(request.POST)
        f.save()
        return redirect("/")
    else:
        f = VehicleForm()
        context = { 'form':f }
        return render(request,"create.html",context)


@permission_required('vehicles.delete_vehicle')
def delete(request,id):
    vehicle = Vehicle.objects.get(id=id)
    vehicle.delete()
    return redirect('/retrieve')

@permission_required('vehicles.change_vehicle')
def update(request,id):
    vehicle = Vehicle.objects.get(id=id)
    if request.method == "POST":
        f = VehicleForm(request.POST,instance=vehicle)
        f.save()
        return redirect("/retrieve")
    else:
        f = VehicleForm(instance=vehicle)
        context = { 'form':f }
        return render(request,"create.html",context)