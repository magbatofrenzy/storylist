from django.shortcuts import render, redirect
from django.http import HttpResponse
from StoryList.models import Item, List


def home_page(request):
    items = Item.objects.all()
    return render(request, 'homepage.html',{'items' : items})
    


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'registration list.html', {'list': list_})


def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(ngender=request.POST['Cgname'],nname =request.POST['rname'],nCategory=request.POST['ncategory'],nTitle =request.POST['ntitle'],nAuthor=request.POST['nauthor'],list=list_)
    return redirect(f'/StoryList/{list_.id}/')

def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(nSynopsis=request.POST['nsynopsis'],list=list_) 
    return redirect(f'/StoryList/{list_.id}/')









