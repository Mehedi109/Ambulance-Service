from django import forms
from .models import article,rent_details
#from . models import userCommentForm
from . models import postComment

class articleForm(forms.ModelForm):
	class Meta:
		model=article
		fields="__all__"

class rent_detailsForm(forms.ModelForm):
	class Meta:
		model=rent_details
		fields="__all__"

'''class userCommentForm(forms.ModelForm):
	class Meta:
		model=userComment
		fields=[
			'name',
			'email',
			'comment',
		]'''

class postCommentForm(forms.ModelForm):
	class Meta:
		model=postComment
		fields=[
			'name',
			'email',
			'comment',
		]
			
'''class replyForm(forms.ModelForm):
	class Meta:
		model=reply
		fields=[
			'email',
			'body'
		]	'''	