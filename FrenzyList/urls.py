from django.conf.urls import url, include
from django.contrib import admin
from StoryList import views 

urlpatterns = [    
    url(r'^$', views.home_page, name='home_page'),    
    url(r'^StoryList/new$', views.new_list, name='new_list'),    
    url(r'^StoryList/(\d+)/$', views.view_list, name='view_item'),    
    url(r'^StoryList/(\d+)/add_item$', views.add_item, name='add_item'),]