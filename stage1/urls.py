"""stage1 URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from profileapp.backends import MyRegistrationView
import contactapp.views

import profileapp.views
import dashapp.views

urlpatterns = [

    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),



    # myprofile
    url(r'^settings/$', profileapp.views.settings, name='settings'),
    url(r'^things/(?P<slug>[-\w]+)/$', profileapp.views.thing_detail, name='thing_detail'),
    url(r'^things/(?P<slug>[-\w]+)/edit/$', profileapp.views.edit_thing, name='edit_thing'),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/create_thing/$', profileapp.views.create_thing, name='registration_create_thing'),

    url(r'^accounts/', include('registration.backends.simple.urls')),
    # mycontact
    url(r"^contact/$", contactapp.views.contact, name="contact"),

    # myupload
    # url(r'^dash/$', myupload.views.Form, name="dash"),
    # url(r'^upload', myupload.views.Upload, name="upload"),

    url(r'^dash/$', dashapp.views.Upload, name="dash"),

    # url(r'^data/$', myfield.views.data, name="data"),

    # terms and refund templates
    url(r'^refund/$', TemplateView.as_view(template_name='refund.html'), name='refund'),
    url(r'^tandc/$', TemplateView.as_view(template_name='tandc.html'), name='tandc'),
    url(r'^pay/$', TemplateView.as_view(template_name='pay.html'), name='pay'),
    url(r'^display/$', TemplateView.as_view(template_name='display.html'), name='display'),

    url(r'^admin/', admin.site.urls),



]