from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
from .models import work
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = TaskForm()

    all_items = work.objects.all()
    return render(request, 'index.html', {'form': form, 'all_items': all_items})

def delete(request, list_id):
    item = get_object_or_404(work, pk=list_id)  
    item.delete()
    return redirect('home')


def toggle(request,list_id):
    item = work.objects.get(pk=list_id)
    item.status = not item.status 
    item.save()
    return redirect('home') 

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    else:
        form = UserCreationForm()


    return render(request,'register.html',{'form':form})

