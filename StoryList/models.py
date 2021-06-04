from django.db import models



class Reader(models.Model):
	Name = models. TextField(default='')
	Gender = models.TextField(default='')
	
	class meta:
		db_table = "reader"

class Category(models.Model):
	nCategory = models.TextField(default='')
	reader = models.ForeignKey(Reader, default=None, on_delete=models.PROTECT)
	
	class meta: 	
		db_table = "category"
  	       
#class Content(models.Model):
	#nTitle = models.TextField(default='')
	#nSynopsis = models.TextField(default='')
	#nStory = models.TextField(default='')
	#nAuthor = models.TextField(default='')
	#category = models.ForeignKey(Category, default=None, on_delete=models.PROTECT)
    	
	#class meta:
		#db_table = "content"
     
#class List(models.Model):
	#nread = models.DateTimeField(default='')          
	#nDate = models.DateTimeField(default='')    
	#content = models.ForeignKey(Content, default=None, on_delete=models.PROTECT)
	
	#class meta:
    		#db_table = "list"

#class Remarks(models.Model):
	#nremarks = models.TextField(default='')
	#content = models.ForeignKey(Content, default=None, on_delete=models.PROTECT)
	
	#class meta: 	
		#db_table = "Feedback"


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



