from django.shortcuts import render
from django.shortcuts import render ,redirect ,get_object_or_404
from .form import CategoryForm
from core import models

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def dashboard(req):
    if req.user.is_authenticated:
        if req.user.is_superuser:
            orders = models.Orders.objects.all()
            return render(req , "dashboard.html" , {"orders":orders})
    return redirect("/")

def category(req):
    if req.user.is_authenticated:
        if req.user.is_superuser:
            data = models.Category.objects.all()
            if req.method == "POST":
                form = CategoryForm(req.POST)
                if form.is_valid:
                    form.save()
                    return redirect("/dashboard/categories")
            else:
                form = CategoryForm()
            return render(req , "category.html",{"form" : form , "data":data})
    else:
        return redirect("/")

def categories(req):
    if req.user.is_authenticated:
        if req.user.is_superuser:
            data = models.Category.objects.all()
            return render(req , "categories.html",{"data":data})
    else:
        return redirect("/")


def delete(req,pk):
    if not req.user.is_authenticated:
        return redirect("/404")
    if req.user.is_superuser:
        item = get_object_or_404(models.Category,pk=pk)
        item.delete()
        return redirect('/dashboard/categories')
    else:
        return redirect('/')


def edit(req,pk):
    if not req.user.is_authenticated:
        return redirect("/404")
    if req.user.is_superuser:
        item = get_object_or_404(models.Category , pk=pk)
        if req.method == 'POST':
            form = CategoryForm(req.POST , instance=item)
            if form.is_valid():
                form.save()
                return redirect("/dashboard/categories")
        else:
            form = CategoryForm(instance=item)
        return render(req , "category.html" , {
            "form":form})
    else:
        return redirect('/')
    

def problem(req,pk):
    if not req.user.is_authenticated:
        return redirect("/404")
    if req.user.is_superuser:
        item = get_object_or_404(models.Orders,pk=pk)
        return render(req ,"order.html", {"order":item})
    else:
        return redirect('/')