from django import forms
from .models import Category, Comment

# class CompanyModelForm(forms.ModelForm):
# 	class Meta:
# 		model  = Category
# 		fields = ['name', 'description', 'category']

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['text',]
