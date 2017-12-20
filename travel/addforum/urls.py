from django.conf.urls import url
from . import views


app_name = 'addforum'

urlpatterns = [
	url(r'^$', views.AddForumFormView.as_view(), name = 'addforum'),
] 