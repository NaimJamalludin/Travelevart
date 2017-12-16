from django.views import generic
from .models import Forum
from .models import Comment
from .forms import CommentForm
from .models import ListForum
from django.shortcuts import render, get_object_or_404, redirect

class ForumIndexView(generic.ListView):
	template_name = 'forum/forumindex.html'
	context_object_name = 'all_forum'

	def get_queryset(self):
		return Forum.objects.all()


class DetailForumView(generic.DetailView):
	model = ListForum
	template_name = 'forum/detail.html'


#addComment
def add_comment(request):
	post = get_object_or_404(ListForum)
	if request.method == 'ListForum':
		form = CommentForm(request.ListForum)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.save()
			return redirect('forum:detail')
	else:
		form = CommentForm()
	template = 'forum/add_comment.html'
	context = {'form': form}
	return render(request, template, context)