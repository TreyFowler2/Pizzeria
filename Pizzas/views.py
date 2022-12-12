from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import *
from datetime import datetime, date

from django.contrib.auth.decorators import login_required
from django.http import Http404


# Create your views here.

# When a URL request matches the pattern we just defined, 
# Django looks for a function called index() in the views.py file. 

def index(request):
    """The home page for Learning Log."""
    return render(request, 'Pizzas/index.html')

@login_required
def profile(request):
    profile = Profile.objects.filter(user=request.user)
    if not profile.exists():
        Profile.objects.create(user=request.user)
    profile = Profile.objects.get(user=request.user)

    if request.method != 'POST':
        form = ProfileForm(instance=profile)
    else:
        form = ProfileForm(instance=profile,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('Pizzas:profile')

    context = {'form': form}
    return render(request, 'Pizzas/profile.html', context)

@login_required
def comments(request, pizza_id):
    if request.method == 'POST' and request.POST.get("btn1"):
        comment = request.POST.get("comment")
        Comment.objects.create(post_id=pizza_id,username=request.user,text=comment,date_added=date.today())

    comments = Comment.objects.filter(post=pizza_id)
    pizza = Pizza.objects.get(id=pizza_id)

    context = {'pizza':pizza, 'comments':comments}

    return render(request, 'Pizzas/comments.html',context)

@login_required
def pizzas(request):
    pizzas = Pizza.objects.order_by('date_added')

    context = {'all_pizzas':pizzas}
    return render(request, 'Pizzas/pizzas.html', context)

@login_required
def pizza(request, pizza_id):
    p = Pizza.objects.get(id=pizza_id)

    toppings = Topping.objects.filter(pizza=p)

    context = {'pizza':p, 'toppings':toppings}
    return render(request, 'Pizzas/pizza.html', context)
