from django.views import generic
from .models import Forum

class ForumIndexView(generic.ListView):
	template_name = 'forum/forumindex.html'
	context_object_name = 'all_forum'

	def get_queryset(self):
		return Forum.objects.all()


class DetailForumView(generic.DetailView):
	model = Forum
	template_name = 'forum/detail.html'

