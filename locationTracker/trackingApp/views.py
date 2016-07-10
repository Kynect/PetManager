from django.shortcuts import render

from .models import Device


def index(request):
	device = Device.objects.get(pk=1)
	deviceLocations = device.location_set.all()

	context = {
		'device': device,
		'deviceLocations': deviceLocations
	}

	return render(request, 'index.html', context)