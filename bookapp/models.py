from django.db import models

class Customer(models.Model):
	'''catchoice= [
        ('education', 'Education'),
        ('entertainment', 'Entertainment'),
        ('comics', 'Comics'),
        ('biography', 'Biographie'),
        ('history', 'History'),
        ]
        #utype=,choices=catchoice,default='education'''
	utype=models.CharField(max_length=100)
	uname=models.CharField(max_length=100)
	uemail=models.EmailField()
	ucontact=models.CharField(max_length=15)
	ulocation=models.CharField(max_length=100)
	udestination=models.CharField(max_length=100)
	udate=models.CharField(max_length=100)
	utime=models.CharField(max_length=100)
	
	class Meta:
		db_table="customer"
			
class Category(models.Model):
	title=models.CharField(max_length=50)

	def __str__(self):
		return self.title

class blog_article(models.Model):
	title=models.CharField(max_length=50)
	posted_on=models.DateTimeField(auto_now=False,auto_now_add=True)
	updated_on=models.DateTimeField(auto_now=True,auto_now_add=False)
	body=models.TextField()
	Category=models.ForeignKey(Category,on_delete=models.CASCADE)
class data(models.Model):
	title=models.CharField(max_length=50)

class ambulance_details(models.Model):
	ambulance_no=models.CharField(max_length=100)
	ambulance_type=models.CharField(max_length=100)
	is_reserved=models.BooleanField(default=False)
		

