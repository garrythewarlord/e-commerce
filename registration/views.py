from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm

from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required

def register_form(request):

	#disable form when logged in
	if request.user.is_authenticated:
		return redirect('home')

	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = UserRegisterForm()
	return render(request, 'registration/register.html', {'form': form})


def login_form(request):

	#disable form when logged in
	if request.user.is_authenticated:
		return redirect('home')

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.success(request, ("There was an error"))
			return redirect('login')
	form = AuthenticationForm()
	return render(request, 'registration/login.html', {'form': form})


@login_required
def log_out(request):
	logout(request)
	return redirect('home')