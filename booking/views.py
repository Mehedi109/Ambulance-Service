from django.shortcuts import render,HttpResponse

def appointment(request):
	if request.method == "POST":
		your_name=request.POST['your-name']
		your_email=request.POST['your-email']
		your_phone=request.POST['your-phone']

		return render(request,'appointment.html',{
			your_name:'your_name',
			your_email: 'your_email',
			your_phone:'your_phone'

			})
	return HttpResponse()

def book(request):
	return render(request,'book.html')
