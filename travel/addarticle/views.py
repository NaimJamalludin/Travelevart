from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ArticleForm
from article.models import Article
from django.shortcuts import render
from .forms import UserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin

class AddArticleFormView(LoginRequiredMixin, TemplateView):
	login_url = "login/"
	template_name = 'addarticle/addarticleform.html'

	def get(self, request):
		form = ArticleForm()
		articles = Article.objects.all()
		args = {'form': form, 'articless': articles}
		return render(request, self.template_name, args)

	def post(self, request):
			form = ArticleForm(request.POST)
			if form.is_valid():
				form.save()
				artist = form.cleaned_data['artist']
				album_title = form.cleaned_data['album_title']
				album_logo = form.cleaned_data['album_logo']
				args = {'form': form, 'artist': artist, 'album_title': album_title, 'album_logo': album_logo}
				return HttpResponseRedirect(reverse('music:musicindex'))

class UserFormView(TemplateView):
	template_name = 'addarticle/registration_form.html'

	def get(self, request):
		form = UserForm()
		args = {'form': form}
		return render(request, self.template_name, args)

	def post(self, request):
		form = UserForm(request.POST)

		if form.is_valid():
			user = form.save(commit=False)

			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			user.set_password(password)
			user.save()

			user = authentication(usrename=username, password=password)

			if user is not None:
				if user.is_active:
					login(request, user)
					return request('music:musicindex')

		return render(request, self.template_name, {'form': form})