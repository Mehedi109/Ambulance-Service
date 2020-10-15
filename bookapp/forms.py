from django import forms
from bookapp.models import Customer
from bookapp.models import blog_article

class CustomerForm(forms.ModelForm):
	class Meta:
		model=Customer
		fields=[
			'utype',
			'uname',
			'uemail',
			'ucontact',
			'ulocation',
			'udestination',
			'udate',
			'utime'
		]

class blog_articleForm(forms.ModelForm):
	class Meta:
		model=blog_article
		fields="__all__"

			
		