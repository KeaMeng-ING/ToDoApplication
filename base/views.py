from django.shortcuts import redirect, render
from .models import Tasks
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        tasks = Tasks.objects.filter(user=request.user)
        uncompleteTask = tasks.filter(complete=False).count()
    else:
        tasks = []
        uncompleteTask = 0

    context = {
        'tasks': tasks, 'uncompleteTask': uncompleteTask
    }
    return render(request, 'base/home.html', context)

def addTask(request):
    if request.method == 'POST':
        task = request.POST['task']
        Tasks.objects.create(title=task, user=request.user)  # title because of the model
    return redirect('home')

def deleteTask(request, pk):
    item = Tasks.objects.get(id=pk)
    item.delete()
    return redirect('home')

def completeTask(request, pk):
    item = Tasks.objects.get(id=pk)
    item.complete = True
    item.save()
    return redirect('home')

def uncompleteTask(request, pk):
    item = Tasks.objects.get(id=pk)
    item.complete = False
    item.save()
    return redirect('home')

def logoutUser(request):
    logout(request)
    return redirect('home')

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')
            # return redirect('login')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'base/login.html', context)


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        User.objects.create_user(username=username, password=password)
        user = authenticate(request, username=username, password=password)

        login(request, user)
        return redirect('home')

    context = {}
    return render(request, 'base/register.html', context)

    