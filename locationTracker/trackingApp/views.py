from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User

from .models import Device


def home(request):
	current_user = request.user
	# device = Device.objects.get(pk=1)
	# deviceLocations = device.location_set.all()

	context = {
		# 'device': device,
		# 'deviceLocations': deviceLocations
	}

	return render(request, 'index.html', context)

def help(request):
	return render(request, 'help.html')

def testimonials(request):
	return render(request, 'testimonials.html')

def about_us(request):
	return render(request, 'about_us.html')

def contact_us(request):
	return render(request, 'contact_us.html')

def purchase(request):
	return render(request, 'purchase.html')

def login(request):
	return render(request, 'login.html')

# def logout(request):
# 	logout(request)

# 	return redirect('/home')


def profile(request):
	if not request.user.is_authenticated():
		return redirect('/home')

	current_user = request.user

	context = {
		# include contexts here
	}

	return render(request, 'profile.html', context)

def notifications(request):
	if not request.user.is_authenticated():
		return redirect('/home')

	current_user = request.user

	context = {
		# include contexts here
	}

	return render(request, 'notifications.html', context)

def account_settings(request):
	if not request.user.is_authenticated():
		return redirect('/home')

	current_user = request.user

	context = {
		# include contexts here
	}

	return render(request, 'account_settings.html', context)

def sign_up(request):
	return render(request, 'sign_up.html')
