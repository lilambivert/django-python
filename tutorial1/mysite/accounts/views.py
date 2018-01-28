from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from mysite import settings

# Create your views here.
def signup_view(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.backend = 'django.contrib.auth.backends.ModelBackend'
			login(request, user)
			return redirect('blog/create_blog')
	else: 
		form = UserCreationForm()
	return render(request, 'accounts/signup.html', {'form':form})

def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return redirect('blog/create_blog')
	else:
		form = AuthenticationForm()
	return render(request, 'accounts/login.html', {'form':form})

def logout_view(request):
	if request.method == 'POST':
		logout(request)
		return redirect('blog/post/')
		#return HttpResponseRedirect(settings.LOGIN_URL)	
	else:
		print request.method
		print "hello get"
		return redirect('blog/create_blog')
