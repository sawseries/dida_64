from django.shortcuts import render, redirect, get_object_or_404
from .models import citizen
from .forms import CitizenForm
from django.views.generic import ListView, DetailView
from django.contrib.postgres.search import SearchVector
from datetime import date
from django.contrib.auth.models import User

def show(request): 
    if User.is_authenticated: 
        citizens = citizen.objects.all()  
        return render(request,"index.html",{'citizens_list':citizens})  
    else:
      return redirect('/login') 

def create(request):  
    if request.method == "POST":  
        form = CitizenForm(request.POST,request.FILES)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')  
            except:  
                pass  
    else:  
        form = CitizenForm()  
    return render(request,'create.html',{'form':form})  
def edit(request, pk, template_name='crudapp/edit.html'):
    citizen = get_object_or_404(citizen, pk=pk)
    form = CitizenForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form':form})

def detail(request, id): 
    citizens = citizen.objects.get(pk=id)
    return render(request,"detail.html",{'citizens':citizens})     

def search(request):
    if request.method=="GET":  
        form = CitizenForm(request.POST)
     
        search_vector = SearchVector('citizen_id', 'firstname', 'lastname')
        return render(request,'search.html',{'form':form}) 
    else:  
        form = CitizenForm()  
        return render(request,'search.html',{'form':form}) 

#def delete(request, pk, template_name='crudapp/confirm_delete.html'):
 #    citizen  = get_object_or_404(citizen, pk=pk)
 #   if request.method == 'POST':
 #        citizen.delete()
 #       return redirect('index')
 #   return render(request, template_name, {'object':citizen})