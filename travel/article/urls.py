from django.conf.urls import url
from . import views

app_name = 'article'

urlpatterns = [

	# Method 2
	url(r'^$', views.ArticleIndexView.as_view(), name = 'articleindex'),

	# Method 2
	url(r'^(?P<pk>[0-9]+)', views.DetailView.as_view(), name = 'detail'),
]