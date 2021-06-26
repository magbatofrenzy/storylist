from django.shortcuts import render, redirect
from django.http import HttpResponse
from StoryList.models import Reader, Category, Stories, List, Remarks
from django.views.decorators.csrf import csrf_exempt


def home_page(request):
    return render(request, 'Home1.html')

def home(request):
    return render(request, 'Home1.html')

def about(request):
    return render(request, 'ABOUT.html')
    
def  page1(request):
    return render(request, 'model1.html')

def  page2(request):
    return render(request, 'model2.html')

def  page3(request):
    return render(request, 'model3.html')

def  page4(request):
    return render(request, 'model4.html')

def  page5(request):
    return render(request, 'model5.html')


# def MainPage(request): Reader
    # nName = nName.objects.all()
    # return render(request, 'model1.html',{'nName' : nName})
# def new_reader(request): Reader
    
    # newreader_ = Reader.objects.create(nName =request.POST['name'],nGender=request.POST['Gender'],nAge=request.POST['Age'])
    # return redirect(f'/{newreader_.id}/')

# def view_reader(request, reader_id):  Category
    # nCategory_ = nCategory.objects.get(id=nCategory_id)
    # return render(request, 'model2.html', {'reader': reader_})

# def add_info(request, reader_id):   Category
    # reader_ = Reader.objects.get(id=reader_id)    
    # Category.objects.create(nCategory=request.POST['nCategory'],NewReader=request.POST['NewReader'])
    # return redirect(f'{reader_.id}/')    

# def edit(request, id):
    # reader =  Reader.objects.get(id=id)
    # context = {'reader':readers }
    # return render(request, 'edit.html', context)

# def update(request, id):
    # reader = nName = request.POST['name']
    # reader = nGender = request.POST['Gender']
    # reader = nAge = request.POST['Age']
    # reader.save()
    # return redirect('/')

# def delete(request, id);
    # reader =  Reader.objects.get(id=id)
    # redear.delete()
    # return redirect('/')












#def view_reader(request):
    #reader = Reader.objects.all()
    # return render(request, 'model1.html', {'reader': reader})


# def new_reader(request):
    # reader_ = Reader.objects.create(Name=request.POST['rname'],Gender =request.POST['F/M'])
    # return redirect(f'/StoryList/{reader_.id}/')

# def add_item(request, reader_id):
    # reader_ = Reader.objects.get(id=id_reader)
    #Category.objects.create(nSynopsis=request.POST['nsynopsis'],reader=list_) 
    # return redirect(f'/StoryList/{reader_.id}/')



# def dataManipulation(request):
#     Reader = (Reader= 'Frenzy Camille Magbato', Gender='Female',Category='Fairytale', Author='Jacob Grimm', Condition='old reader', Remarks='finished')
#     reader.save()

#     Read All Entries
#     objects = reader.objects.all
#     result = 'Printing all entries in reader model : <br>'
#     for x in objects:
#             #res +.Choices+'<br>'

#     Read a specific entry:
#     name = reader.objects.get()
#     res += 'printing one entry  <br>'
#     res += reader.Name


#     #Delete an entry
#     res += '<br> Deleting an entry <br>'
#     name.delete()

#     #Update
#     Reader = reader(Name='Carolyn Quillope', Gender='Female', Category='Adventure', Author='Nicholas Monsarrat', Condition='new reader', Remarks= 'unfinished')
#     reader.save()
#     res += 'Updating entry <br>'

#     reader = Reader.objects.get(reader = Carolyn Quillope)
#     reader. CChoices = "Adventure"
#     reader.save()
#     res = ""

#     #Filtering data:
#     qs = Reader.objects.filter(Reader = Carolyn Quillope)
#     res += "new reader: %s results <br>" %len(qs)

#     #Ordering results:
#     qs = Reader.objects.order_by('Remarks')
#     for x in qs:
#             res += xReader + x.Remarks +'<br>'

