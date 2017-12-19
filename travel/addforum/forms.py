from django import forms
from forum.models import Forum

class ForumForm(forms.ModelForm):
	class Meta:
		model = Forum
		fields = ('forum_title','forum_items')