from django.views.generic import ListView
from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q

from . models import Category
from . models import Quot
from . models import ability_top
from . models import ability_bottom
from . models import slider

from . models import service_category
from . models import service_section

from .models import service_area
from .models import service_area_body
from .models import border_top
from .models import border_bottom

#from . forms import articleForm
from .forms import articleForm
from .models import article
'''from .models import user'''

from .forms import rent_detailsForm
from . models import rent_details
#from .forms import userCommentForm
#from . models import userComment
from . models import freezer,general,ICU,emergency
from .models import postComment
from .forms import postCommentForm

#from .models import reply
#from .forms import replyForm


class HomeView(ListView):
	template_name="index.html"
	model=Quot
	#model=service_category
	#model=service_section
	
	def get_queryset(self):
		query_set=super().get_queryset()
		return query_set.select_related
		('Category')


def index(request):
	post=service_category.objects.all
	content=service_section.objects.all
	quote=Quot.objects.all
	s_a_c=service_area.objects.all
	s_a_b=service_area_body.objects.all
	slider_post=slider.objects.all
	border_top_post=get_object_or_404(border_top)
	#border_bottom_post=border_bottom.objects.all
	border_bottom_post=border_bottom.objects.all
	ability_top_post=get_object_or_404(ability_top)
	ability_bottom_post=ability_bottom.objects.all
	emergency_post=get_object_or_404(emergency)
	context={
		"post":post,
		"content":content,
		"quote":quote,
		"s_a_c":s_a_c,
		"sab":s_a_b,
		"post2":border_top_post,
		"border_bottom_post":border_bottom_post,
		"post3":ability_top_post,
		"ability_bottom_post":ability_bottom_post,
		#"post4":ability_bottom_post
		"slider_post":slider_post,
		"post4":emergency_post,
	}
	return render (request,"index.html",context)
def terms(request):
	quote=Quot.objects.all
	post2=slider.objects.all()
	context={
		"quote":quote,
		"post2":post2
	}
	return render(request,"terms.html",context)
def ac_post(request):
	post=get_object_or_404(general)
	post2=slider.objects.all
	context={
		"post":post,
		"post2":post2
	}
	return render(request,"ac.html",context)

def general_post(request):
	post=get_object_or_404(freezer)
	post2=slider.objects.all
	context={
		"post":post,
		"post2":post2
	}
	return render(request,"general.html",context)
def icu_post(request):
	post=get_object_or_404(ICU)
	post2=slider.objects.all
	context={
		"post":post,
		"post2":post2
	}
	return render(request,"icu.html",context)

def contact(request):
	return render(request,"contact.html")
	
def post(request):
	if request.user.is_authenticated:
		form=articleForm(request.POST or None)
		if form.is_valid():
			instance=form.save(commit=False)
			instance.save();
			return redirect('/blog')
	return render (request,"post.html",{"form":form})

def post_update(request,id):
	#if request.user.is_authenticated:
	if request.user.is_staff or request.user.is_superuser:
		post=get_object_or_404(article,id=id)
		#post=article.objects.get(id=id)
		form=articleForm(request.POST or None,instance=post)
		if form.is_valid():
		   instance=form.save(commit=False)
		   instance.save()
		   #messages.success(request,'Updated Successfully')
		   return redirect('/author_blog')
		return render(request,"post.html",{"form":form})
	return HttpResponse()

def blog_update(request,id):
		post=get_object_or_404(article,id=id)
		#post=article.objects.get(id=id)
		return redirect('/blog')
		return render(request,"blog.html",{"post":post})
	  #return HttpResponse()

def delete(request,id):
	#if request.user.is_authenticated:
	if request.user.is_staff or request.user.is_superuser:
		post=get_object_or_404(article,id=id)
		post.delete()
		return redirect('/author_blog')

def blog(request):
	post=article.objects.all().order_by('id')
	##post=get_object_or_404(article,id=id)
	#getComment=userComment.objects.filter()
	#form=userCommentForm(request.POST or None)
	#if form.is_valid():
		#instance=form.save(commit=False)
		#instance.post=post
		#instance.save()
	context={
		"post":post,
		#"form":form,
		#"comment":getComment
	}
	return render(request,"blog.html",context)
	#return HttpResponse()
def single_blog(request,id):
	#post=article.objects.all()
	#post=article.objects.get(id=id)
	post=get_object_or_404(article,id=id)
	#post=article.objects.get(id=postid)
	getComment=postComment.objects.filter(post=id)
	'''getComment=userComment.objects.filter(post=id)#reply=none  user''' 
	#getReply=reply.objects.filter(post=id)
	if request.method=="POST":
		form=postCommentForm(request.POST or None)
		'''form=userCommentForm(request.POST or None)  user'''
		if form.is_valid():
			instance=form.save(commit=False)
			instance.post=post
			parent_id = request.POST.get('comment_id') #reply-section
			comment_qs=None
			if parent_id:
				comment_qs = postComment.objects.get(id=parent_id)
			instance.save()
			'''parent_obj=None
			try:
				parent_id=int(request.POST.get('parent_id'))
			except:
				parent_id=None
			if parent_id:
				parent_obj=postComment.objects.get(parent_id)
				if parent_obj:
					replay_comment=form.save(commit=False)
					replay_comment.parent=parent_obj'''
			'''reply_id = request.POST.get('comment_id') #reply-section
			comment_qs=None
			if reply_id:
				comment_qs = userComment.objects.get(id=reply_id)
			comment = userComment.objects.create(post=post, user=request.user, content=content, reply=comment_qs)
			comment.save()'''
			return redirect('single_blog',id)
	else:	
		'''form=userCommentForm()  user'''
		form=postCommentForm()
		context={
			"post":post,
			"form":form,
			"comment":getComment,
			#"reply":replay_comment,
			#"comment":getComment,  user
		}
	return render(request,"single_blog.html",context)
		#return HttpResponse()
def post_comment(request,id):
	if request.method=="POST":
		comment=request.POST.get("comment")
		postid=request.POST.get("postid")
		post=article.objects.get(id=postid)
		parentid=request.POST.get("parentid")
		if parentid== "":
			comment=postComment(comment=comment,post=post)
		else:
			parent=postComment.objects.get(id=parentid)
			comment=postComment(comment=comment,post=post,parent=parent)
		comment.save()
		return redirect('single_blog',id)
	return render(request,"single_blog.html",context)	
def comment_delete(request,id):
	post=get_object_or_404(postComment,id=id)
	post.delete()
	return redirect('single_blog',id)
	return HttpResponse()

def rent_show(request):
	post=rent_details.objects.all()
	search=request.POST.get('q')
	if search:
		post=post.filter(
			Q(From__icontains=search)
			)
	paginator = Paginator(post, 5) # Show 25 contacts per page.
	page = request.GET.get('page')
	total_post = paginator.get_page(page)
	context={
		#"post":post,
		"post":total_post	
	}
	return render(request,"rent.html",context)

def rent(request):
	#post=get_object_or_404(rent_details,id=id)
	post=rent_details.objects.all()
	first=rent_details.objects.first()
	last=rent_details.objects.last()
	search=request.POST.get('q')
	if search:
		post=post.filter(
			Q(From__icontains=search) |
			Q(To__icontains=search)
			)
	paginator = Paginator(post, 10) # Show 25 contacts per page.
	page = request.GET.get('page')
	total_post = paginator.get_page(page)
	context={
		"post":total_post,
		"first":first,
		"last":last,
	}
	return render(request,"rent.html",context)

def rent_post(request):
	if request.user.is_authenticated:
		form=rent_detailsForm(request.POST or None)
		if form.is_valid():
			instance=form.save(commit=False)
			instance.save();
			return redirect('/author_rent')
	return render (request,"rental.html",{"form":form})

def rent_update(request,id):
	if request.user.is_authenticated:
		post=get_object_or_404(rent_details,id=id)
		#post=article.objects.get(id=id)
		form=rent_detailsForm(request.POST or None,instance=post)
		if form.is_valid():
		   instance=form.save(commit=False)
		   instance.save()
		   return redirect('/author_rent')
		return render(request,"rental.html",{"form":form})
	return HttpResponse()

def rent_delete(request,id):
	if request.user.is_authenticated:
		post=get_object_or_404(rent_details,id=id)
		post.delete()
		return redirect('/author_rent')
