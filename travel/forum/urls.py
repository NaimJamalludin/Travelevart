from django.conf.urls import url
from . import views

app_name = 'forum'

urlpatterns = [

	# Method 2
	url(r'^$', views.ForumIndexView.as_view(), name = 'forumindex'),

	# Method 2
	url(r'^(?P<slug>[-\w]+)/$', views.DetailForumView.as_view(), name = 'detail'),


	url(r'^(?P<slug>[-\w]+)/comment/$', views.add_comment, name='add_comment'),
]