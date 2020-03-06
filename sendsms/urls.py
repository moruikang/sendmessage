from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^hello', views.hello, name='hello'),
    url(r'^sms', views.sendsms, name='sendsms'),
    url(r'^email', views.sendemail, name='sendemail'),
]