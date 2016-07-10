from django.conf.urls import url

from . import views

app_name = 'trackingApp'
urlpatterns = [
	# ex: /trackingApp/
    url(r'^$', views.index, name='index'),
]