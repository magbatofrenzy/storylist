from django.conf.urls import url, include
from django.contrib import admin
from StoryList import views 

urlpatterns = [  
    url(r'^$', views.home_page,  name='home_page'),
    url(r'^home/',  views.home,  name='home'),
    url(r'^about/', views.about, name='about'),      
    url(r'^page1/', views.page1, name='page1'),    
    url(r'^page2/', views.page2, name='page2'), 
    url(r'^page3/', views.page3, name='page3'),
    url(r'^page4/', views.page4, name='page4'),  
    url(r'^page5/', views.page5, name='page5'),]


    
# url(r'^$', views.home_page, name='home_page'),    
    # url(r'^$StoryList/new_category$', views.new_reader, name='new_reader'),        
    # url(r'^$StoryList/(\d+)/$', views.view_reader, name='view_reader'),    
    # url(r'^$StoryList/(\d+)/new_category$', views.new_category, name='new_category')   
