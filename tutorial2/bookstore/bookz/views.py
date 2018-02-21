from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Book
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from bookstore import settings
from .forms import PurchaseForm
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method =='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/bookz/home')
    else:
        form = AuthenticationForm()
    return render(request, 'bookz/login.html', {'form':form})

@login_required(login_url="/bookz/login/")
def purchase_view(request, id):
    book = Book.objects.get(id=id)
    user = request.user
    if(request.method == 'POST'):
        form = PurchaseForm(request.POST)
        if form.is_valid():
            z = form.save(commit=False)
            z.book = book
            z.price = book.price
            z.user = request.user
            z.save()
        return redirect('/bookz/home')
    else:
        form = PurchaseForm()
    return render(request, 'bookz/purchase.html', {'form':form, 'book':book, 'user': user})

def home_view(request):
    books = Book.objects.all()

    context = {
        'books':books
    }

    return render(request, 'bookz/home.html', context)
