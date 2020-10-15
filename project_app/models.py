from django.db import models
#from django.contrib.auth.models import User

class Category(models.Model):
	title=models.CharField(max_length=50)

	def __str__(self):
		return self.title

class Quot(models.Model):
	quote=models.TextField()
	title=models.CharField(max_length=50)	

	quote_category=models.ForeignKey(
		'Category',
		on_delete=models.CASCADE
		)
	def __str__(self):
		return self.quote
	#def __str__(self):
		#if len(self.quote)>50:
			#return self.quote[:50]+"..."
		#return self.quote



class service_category(models.Model):
	title=models.CharField(max_length=50)

	def __str__(self):
		return self.title

	subtitle=models.CharField(max_length=50)
	#name=models.CharField(max_length=50)

	
class service_section(models.Model):
	servicetitle=models.CharField(max_length=50)
	content=models.TextField()	


	#content_category=models.ForeignKey(
		#'service_category',
		#on_delete=models.CASCADE
		#)
class slider(models.Model):
	image=models.FileField()

class service_area(models.Model):
	title=models.CharField(max_length=50)
	short_desc=models.TextField()

class service_area_body(models.Model):
	image=models.FileField()
	title=models.CharField(max_length=50)
	content=models.TextField()

class article(models.Model):
	title=models.CharField(max_length=50,unique=True)
	posted_on=models.DateTimeField(auto_now=False,auto_now_add=True)
	updated_on=models.DateTimeField(auto_now=True,auto_now_add=False)
	body=models.TextField()
	Category=models.ForeignKey(Category,on_delete=models.CASCADE)

class rent_details(models.Model):
	From=models.CharField(max_length=100)
	To=models.CharField(max_length=100)
	General_Rent=models.CharField(max_length=100)
	Freezer_Rent=models.CharField(max_length=100)
	ICU_Rent=models.CharField(max_length=100)
	
	def __str__(self):
		return self.From


class postComment(models.Model):
	post=models.ForeignKey(article,on_delete=models.CASCADE)
	name=models.CharField(max_length=100)
	email=models.EmailField(max_length=100)
	comment=models.TextField()
	parent=models.ForeignKey('postComment',null=True,related_name="replies",on_delete=models.CASCADE)
#return 'comment  by'.format(self.body self.name)
'''class reply(models.Model):
	post=models.ForeignKey(userComment,on_delete=models.CASCADE)
	email=models.EmailField(max_length=100)
	body=models.TextField()'''	

class border_top(models.Model):
	title=models.CharField(max_length=100)
	subtitle=models.CharField(max_length=100)

class border_bottom(models.Model):
	title=models.CharField(max_length=100)
	content=models.TextField()

class ability_top(models.Model):
	title=models.CharField(max_length=100)
	subtitle=models.CharField(max_length=100)

class ability_bottom(models.Model):		
	content=models.TextField()

class emergency(models.Model):
	h2_title=models.CharField(max_length=100)
	span_title=models.CharField(max_length=100)
	last_title=models.CharField(max_length=100)
	desc=models.TextField()
	phone=models.CharField(max_length=20)
	image=models.FileField()
class general(models.Model):
	title=models.CharField(max_length=100)
	content=models.TextField()
	image=models.FileField()

class freezer(models.Model):
	title=models.CharField(max_length=100)
	content=models.TextField()
	image=models.FileField()

class ICU(models.Model):
	title=models.CharField(max_length=100)
	content=models.TextField()
	image=models.FileField()
		
				