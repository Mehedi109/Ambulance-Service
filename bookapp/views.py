from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from bookapp.forms import CustomerForm
from bookapp.models import Customer
from project_app.models import article
from project_app.forms import articleForm
from project_app.models import rent_details
from bookapp.forms import blog_articleForm
from bookapp.models import blog_article
from .models import ambulance_details
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import Q

def emp(request):
	if request.method == "POST":
		form=CustomerForm(request.POST)
		if form.is_valid():
			try:
				if request.user.is_authenticated:
					form.save()
					messages.success(request,'Booked Successfully')
					return redirect("/emp")

				else:
					messages.info(request,'Please login your account')
					return redirect('login')
					if user is not None:
						auth.login(request,user)
						return redirect('/emp')
			except:
				pass
	else:
		form=CustomerForm()
		return render(request,"bookindex.html",{"form":form})
	return HttpResponse()
def ambulance(request):
	items=ambulance_details.objects.all().order_by('id')
	item=ambulance_details.objects.get('id')
	def __init__(self):
	       self.items = []
	def enqueue(self,item):
	       self.items.insert(0,item)
	def dequeue(self):
	       self.items.pop()
	def is_empty(self):
	        if len(self.items) == 0:
	            return True
	        else:
	            return False
def show(request):
	customers=Customer.objects.all().order_by('id')
	messages.warning(request,'Sorry, you are not authorized to access this page')
	#alldata=Customer.objects.all().order_by('created_at')
	post=article.objects.all().order_by('id')
	context={
		"customers":customers,
		"post":post
	}
	return render(request,"show.html",context)
def author(request):
	#messages.warning(request,'Sorry, you are not authorized to access this page')	
	return render(request,"show.html")
def author_book(request):
	customers=Customer.objects.all().order_by('id')
	search=request.POST.get('q')
	if search:
		customers=customers.filter(
			Q(ulocation__icontains=search)
			)
	return render(request,"author_book.html",{'customers':customers})
def author_blog(request):
	post=article.objects.all().order_by('id')
	return render(request,"author/author_blog.html",{'post':post})
def author_rent(request):
	post=rent_details.objects.all().order_by('id')
	search=request.POST.get('q')
	if search:
		post=post.filter(
			Q(From__icontains=search)|
			Q(To__icontains=search)
			)
	return render(request,"author/author_rent.html",{'post':post})		
def home(request):
	customers=Customer.objects.all()
	return render(request,"home.html",{'customers':customers})
def edit(request,id):
	customer=Customer.objects.get(id=id)
	return render(request,"edit.html",{"customer":customer})

#def post(request):
	#if request.user.is_authenticated:
		#form=blog_articleForm(request.POST or None)
		#if form.is_valid():
			#instance=form.save(commit=False)
			#instance.save();
			#return redirect('blog')
	#return render (request,"post.html",{"form":form})


def post_edit(request,id):
	#post=article.objects.get(id=id) 
	form=blog_articleForm(request.POST or None)
	Model.objects.all().order_by("created_at")
	return render(request,"post_edit.html",{"form":form})
	
def update(request,id):
	customer=Customer.objects.get(id=id)
	form=CustomerForm(request.POST,instance=customer)
	if form.is_valid():
	   form.save()  
	   return redirect("/author_book")
	   return render(request,"edit.html",{"customer":customer})
	   return HttpResponse()
	#else:
		#return redirect('/')
	#return HttpResponse()
	
#def blog(request):
	#post=article.objects.all()
	#context={
		#"post":post
	#}
	#return render(request,"blog.html",context)


def delete(request,id):
	customer=Customer.objects.get(id=id)
	customer.delete()
	return redirect('/author_book')
	


