from django.conf.urls import url
from . import views

app_name = 'forum'

urlpatterns = [

	# Method 2
	url(r'^', views.ForumIndexView.as_view(), name = 'forumindex'),

	# Method 2
	url(r'^(?P<pk>[0-9]+)', views.DetailView.as_view(), name = 'detail'),
]