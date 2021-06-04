from django.conf.urls import url, include
from django.contrib import admin
from StoryList import views 

urlpatterns = [    
    url(r'^$', views.home_page, name='home_page'),    
    url(r'^StoryList/new$', views.new_reader, name='new_reader'), 
    url('admin/', admin.site.urls),   
    url(r'^StoryList/(\d+)/$', views.view_reader, name='view_reader'),    
    url(r'^StoryList/(\d+)/add_item$', views.add_item, name='add_item')]