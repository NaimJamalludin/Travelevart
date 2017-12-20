from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ForumForm
from forum.models import Forum
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin

class AddForumFormView(LoginRequiredMixin, TemplateView):
	login_url = "login/"
	template_name = 'addforum/addforum.html'

	def get(self, request):
		form = ForumForm()
		forums = Forum.objects.all()
		args = {'form': form, 'forums': forums}
		return render(request, self.template_name, args)

	def post(self, request):
			form = ForumForm(request.POST)
			if form.is_valid():
				forum = form.save(commit = False)
				forum_title = form.cleaned_data['forum_title']
				forum_items = form.cleaned_data['forum_items']
				forum.save()
				form.save_m2m()
				args = {'form': form, 'forum_title': forum_title, 'forum_items': forum_items}
				return HttpResponseRedirect(reverse('forum:forumindex'))
