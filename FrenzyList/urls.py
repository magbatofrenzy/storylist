from django.conf.urls import url, include
from django.contrib import admin
from StoryList import views 

urlpatterns = [  
    url(r'^$', views.home_page,  name='home_page'),
    url(r'^home/',  views.home,  name='home'),
    url(r'^about/', views.about, name='about'),      
    url(r'^page12/', views.page12, name='page12'),    
    url(r'^page345/', views.page345, name='page345'), 
    url(r'^$', views.home_page, name='home_page'),    
    url(r'^new_reader$', views.new_reader, name='new_reader'),        
    url(r'^(\d+)/view_reader$', views.view_reader, name='view_reader'),    
    url(r'^(\d+)/new_category$', views.new_category, name='new_category'),  
    url(r'^edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),]