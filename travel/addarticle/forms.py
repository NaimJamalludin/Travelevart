#from django import forms

#class MusicForm(forms.Form):
#	album_name = forms.CharField(label='Album Name', max_length=100)


from django.forms import ModelForm
from article.models import Article
from django import forms
from django.contrib.auth.models import User

class ArticleForm(ModelForm):

	class Meta:
		model = Article
		fields = ('__all__')

class UserForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput)
	class  Meta:
		model = User
		fields = ['username', 'email', 'password']
