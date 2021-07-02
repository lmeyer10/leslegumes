from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/', views.index, name='index'),
    url(r'^menu/', views.menu, name='menu'),
    url(r'^reviews/', views.reviews, name='reviews'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^reserve/', views.reserve, name='reserve'),
    url(r'^submit-received/', views.submitreceived, name='submit-received'),
]

