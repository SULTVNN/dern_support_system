from django.shortcuts import render ,redirect , get_object_or_404
from .form import SignUpForm , CategoryForm , ProblemForm
from . import models
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(req):
    return render(req , "welcome.html")

def signup(req):
    if req.method == 'POST':
        form = SignUpForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = SignUpForm()
    
    return render(req , "signup.html",{
        'form':form
    })
def faq(req):
    return render(req , 'FAQ.html')


def logout_view(req):
    if not req.user.is_authenticated:
        return redirect("/404")
    logout(req)
    return redirect('/')

def profile(req):
    if not req.user.is_authenticated:
        return redirect("/404")
    if req.user.is_authenticated:
        data = models.Orders.objects.filter(user_id=req.user.id)
        return render(req , "profile.html" , {"data" : data})
    return redirect("/")


def book(req):
    if not req.user.is_authenticated:
        return redirect("/404")
    if req.method == 'POST':
        form = ProblemForm(req.POST , user=req.user.id)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = req.user  # Assign user value
            order.save()
            return redirect('/profile')
    else:
        form = ProblemForm()
    return render(req , "problem.html" , {"form" : form})
def errorr(req):
    return render(req , "required.html")