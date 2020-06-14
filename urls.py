from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from .import views
from .models import post
app_name = 'blog'
urlpatterns=[
path('',views.post_list,name='list'),
    path('create/',views.post_create,name='post_create'),
path('',views.post_contact,name='post_contact'),
    url(r'^(?P<id>\d+)/delete/$',views.post_delete,name='post_delete'),
url(r'^(?P<id>\d+)/$',views.post_detail,name='detail'),
url(r'^(?P<id>\d+)/edit/$',views.post_update,name='update'),
 ]
