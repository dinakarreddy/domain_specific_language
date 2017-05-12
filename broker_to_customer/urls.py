from django.conf.urls import patterns, url

from broker_to_customer import views

urlpatterns = patterns('',
                       url(r'^get_brokers$', views.get_brokers),)