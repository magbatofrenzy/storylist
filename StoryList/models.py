from django.db import models



class Reader(models.Model):
	nName = models. TextField(default='')
	nGender = models.TextField(default='')
	nAge =models.TextField(default='')
	
	class meta:
		db_table = "reader"

class Category(models.Model):
	nCategory = models.TextField(default='')
	NewReader = models.ForeignKey(Reader, default=None, on_delete=models.PROTECT)

	class meta: 	
		db_table = "category"
  	       
class Stories(models.Model):
	nTitle = models.TextField(default='')
	nAuthor = models.TextField(default='')
	Category = models.ForeignKey(Category, default=None, on_delete=models.PROTECT)
    	
	class meta:
		db_table = "stories"
     
class List(models.Model):
	Newreader = models.DateTimeField(default='')             
	Condition = models.ForeignKey(Stories, default=None, on_delete=models.PROTECT)
	
	class meta:
    		db_table = "list"

class Remarks(models.Model):
	finished = models.TextField(default='')
	unfinished = models.ForeignKey(List, default=None, on_delete=models.PROTECT)
	
	class meta: 	
		db_table = "remarks"


'''


# Create your models here.
class Choices(models.Model):
      item = models.ForeignKey(Item, default=None, on_delete = models.CASCADE)
      Fairytale = models. Textfield (default="")
      Adventure = models. Textfield(default="")
      class meta :
		db table = "Choices"


class Author (models.Model):
      firt_name = models.ManytoMany(Author, default=None, on_delete = models.CASCADE)
      last_name = models.Charfield(default="")
      class meta:
	    db_table = "author"


class Condition (models.Model):
	newreader = models.Textfield(Condition, default=None, on_delete = models.CASCADE)
	oldreader = models.Textfield(default="")
	class meta:
		db_table = "conditon"
		
		'''







# Create your models here.



