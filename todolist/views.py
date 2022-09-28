from email import message
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from todolist.models import Task
from todolist.forms import DataUser
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from todolist.forms import DataUser

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    username = request.user.username
    user_id = request.user.id
    tasks = Task.objects.filter(user_id=user_id)
    context = { 
        "username": username,
        "todolist": tasks
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def create_task(request):
    if request.method == "POST":
        form = DataUser(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            return HttpResponseRedirect(reverse('todolist:show_todolist'))
        else:
            message.info(request, 'Data Anda salah')
    else:
        form = DataUser()
    context = { 'form':form }
    return render(request, 'create_task.html', context)

@login_required(login_url='/todolist/login/')
def update_status(request, id):
    update_status = Task.objects.get(id = id)
    if update_status.is_finished:
        update_status.is_finished = False
    else:
        update_status.is_finished = True
    update_status.save()
    return HttpResponseRedirect("/todolist")

@login_required(login_url='/todolist/login/')
def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()

    return HttpResponseRedirect("/todolist")
