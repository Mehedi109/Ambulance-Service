from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
#from django.http import HttpResponse

def login(request):
	if request.user.is_authenticated:
		return redirect('/')
	else:
		if request.method=='POST':
			username=request.POST['username']
			password=request.POST['password']

			user=auth.authenticate(username=username,password=password)

			if user is not None:
				auth.login(request,user)
				return redirect('/')
			else:
				messages.error(request,'Username or Password is incorrect')
				return redirect('login')

		else:
		 	return render(request,'login.html')

def admin_login(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']

		user=auth.authenticate(username=username,password=password)

		if user is not None:
			auth.login(request,user)
			return redirect('/show')
		else:
			messages.error(request,'Username or Password is incorrect')
			return redirect('login')

	else:
		 return render(request,'admin_login.html')	

def register(request):
	if request.method=='POST':
		first_name=request.POST['first_name']	
		last_name=request.POST['last_name']
		username=request.POST['username']	
		email=request.POST['email']	
		password=request.POST['password']	
		password2=request.POST['password2']	
		#if first_name or last_name is empty:
			#messages.info(request,'please fill up the field')
			#return redirect(register)
		#else:
		if password==password2:
			if User.objects.filter(username=username).exists():
				#print('Username Taken')
				#if User.objects.filter(username=self.cleaned_data['username']).exists():
				messages.error(request,'Username Taken')
				return redirect('register')
			elif User.objects.filter(email=email).exists():
				print('Email Taken')
			else:
				user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
				user.save();
				print('user created')
				return redirect('login')
		else:
				messages.info(request,'password not matching')
				return redirect('register')
				return redirect('/')
	else:
	    return render(request,'register.html')
	#return HttpResponse()

def admin_register(request):
	if request.method=='POST':
		first_name=request.POST['first_name']	
		last_name=request.POST['last_name']
		username=request.POST['username']	
		email=request.POST['email']	
		password=request.POST['password']	
		password2=request.POST['password2']	
		#if first_name or last_name is empty:
			#messages.info(request,'please fill up the field')
			#return redirect(register)
		#else:
		if password==password2:
			if User.objects.filter(username=username).exists():
				print('Username Taken')
			elif User.objects.filter(email=email).exists():
				print('Email Taken')
			else:
				user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
				user.save();
				print('user created')
				return redirect('login')
		else:
				messages.info(request,'password not matching')
				return redirect('admin_register')
				return redirect('/')
	else:
	    return render(request,'admin_register.html')
	#return HttpResponse()
	
def logout(request):
	auth.logout(request)
	return redirect('/')

def admin_logout(request):
	auth.logout(request)
	return redirect('/')
