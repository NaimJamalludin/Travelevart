from django.db import models

# Create your models here.
class ListForum(models.Model):
	itemlist = models.CharField(max_length = 1500)
	def __str__(self):
		return self.itemlist

class Forum(models.Model):
    forum_title = models.CharField(max_length = 250)
    content = models.TextField()
    images = models.ImageField(blank=True)
    forum_items = models.ManyToManyField(ListForum)
    def __str__(self):
        return self.forum_title
		