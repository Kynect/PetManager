"""locationTracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
import trackingApp.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', trackingApp.views.home, name="home"),
	url(r'^home/', trackingApp.views.home),
    url(r'^help/', trackingApp.views.help),
    url(r'^about_us/', trackingApp.views.about_us),
    url(r'^contact_us/', trackingApp.views.contact_us),
    url(r'^purchase/', trackingApp.views.purchase),
    url(r'^login/$', trackingApp.views.login, {'template_name': 'login.html'}),
    url(r'^logout/', trackingApp.views.logout, {'next_page': '/home'}),
    url(r'^profile/', trackingApp.views.profile),
    url(r'^notifications/', trackingApp.views.notifications),
    url(r'^account_settings/', trackingApp.views.account_settings),
    url(r'^sign_up/', trackingApp.views.sign_up),
]
