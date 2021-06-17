from django.conf.urls import url, include
from django.contrib import admin
from StoryList import views 

    
urlpatterns = [    
    url(r'^$', views.home_page, name='home_page'),         
    url('page1/', views.page1, name='page1'),    
    url('page2/', views.page2, name='page2'), 
    url('page3/', views.page3, name='page3'), 
    url('page4/', views.page4, name='page4'),  
    url('page5/', views.page5, name='page5'), ]