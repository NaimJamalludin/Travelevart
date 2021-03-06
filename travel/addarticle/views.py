from django.views.generic import TemplateView
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ArticleForm
from article.models import Article
from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class AddArticleFormView(LoginRequiredMixin, TemplateView):
	login_url = "login/"
	template_name = 'addarticle/addarticleform.html'

	def get(self, request):
		form = ArticleForm()
		articles = Article.objects.all()
		args = {'form': form, 'articles': articles}
		return render(request, self.template_name, args)

	def post(self, request):
			form = ArticleForm(request.POST)
			if form.is_valid():
				article = form.save(commit = False)
				article_title = form.cleaned_data['article_title']
				description = form.cleaned_data['description']
				content = form.cleaned_data['content']
				article.author = request.user.username
				# date_published = form.cleaned_data['date_published']
				# thumbnail = form.cleaned_data['thumbnail']
				# header = form.cleaned_data['header']
				article.save()
				args = {'form': form, 'article_title': article_title, 'description': description, 'content': content }
				return redirect('article:articleindex')

class MemberView(generic.ListView):
	template_name = 'addarticle/memberlist.html'
	context_object_name = 'all_user'

	def get_queryset(self):
		return User.objects.all()
		

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

			user = authenticate(username=username, password=password)

			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('article:articleindex')

		return render(request, self.template_name, {'form': form})