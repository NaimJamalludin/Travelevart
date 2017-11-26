from django.views import generic
from .models import Article

class ArticleIndexView(generic.ListView):
	template_name = 'article/articleindex.html'
	context_object_name = 'all_article'

	def get_queryset(self):
		return Article.objects.all()


class DetailView(generic.DetailView):
	model = Article
	template_name = 'article/detail.html'

