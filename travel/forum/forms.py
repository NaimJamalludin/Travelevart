from django import forms
from .models import Comment,Forum

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('user', 'email', 'body')

class ForumForm(forms.ModelForm):
	class Meta:
		model = Forum
		fields = ('forum_title','forum_items')