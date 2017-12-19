from django.db import models
from django.utils import timezone
#from django.core.urlresolvers import reverse
from django.urls import resolve, reverse
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from django.template.defaultfilters import slugify
import datetime

# Create your models here.
class ListForum(models.Model):
	itemlist = models.CharField(max_length = 1500)
	slug = AutoSlugField(populate_from = 'itemlist',unique=True)


	def get_absolute_url(self):
		return reverse('forum:detail',args=[self.slug])


	def __str__(self):
		return self.itemlist

class Forum(models.Model):
    forum_title = models.CharField(max_length = 250)
    #slug = AutoSlugField(populate_from = 'forum_title',unique=True)
    #content = models.TextField()
    #images = models.ImageField(blank=True)
    forum_items = models.ManyToManyField(ListForum)
    def __str__(self):
        return self.forum_title

class Comment(models.Model):
	post = models.ForeignKey(ListForum,on_delete = models.CASCADE,related_name='comments')
	user = models.CharField(max_length=250)
	email = models.EmailField()
	body = models.TextField(max_length=250)
	created = models.DateTimeField(auto_now_add=True)
	approved = models.BooleanField(default=False)

	def approved(self):
		self.approved = True
		self.save()

	def __str__(self):
		return self.user 
		