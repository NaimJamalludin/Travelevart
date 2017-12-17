from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ArticleForm
from article.models import Article
from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin

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
				author = form.cleaned_data['author']
				content = form.cleaned_data['content']
				date_published = form.cleaned_data['date_published']
				args = {'form': form, 'article_title': article_title, 'description': description, 'author': author, 'content': content, 'date_published': date_published}
				return HttpResponseRedirect(reverse('article:articleindex'))

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