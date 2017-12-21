from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout


app_name = 'addarticle'

urlpatterns = [
	url(r'^$', views.AddArticleFormView.as_view(), name = 'addarticle'),
	url(r'^register/$', views.UserFormView.as_view(), name = 'register'),
	url(r'^login/$', login, {'template_name': 'addarticle/login.html'}, name = 'login'),
	url(r'^logout/$', logout, name='logout'),
	url(r'^allusers/$', views.MemberView.as_view(), name = 'allusers'),
] 