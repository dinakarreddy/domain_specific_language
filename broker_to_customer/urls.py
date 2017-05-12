from django.conf.urls import patterns, url

from broker_to_customer import views

urlpatterns = patterns('',
                       url(r'^get_brokers$', views.get_brokers),
                       url(r'^get_flats$', views.get_flats),
                       url(r'^store_user_token$', views.store_user_token),
                       url(r'^store_user_requirement$', views.store_user_requirement),)
