from django.db import models

# Create your models here.
class Tags(models.Model):
	label = models.CharField(max_length = 30)

	def __str__(self):
		return self.label

class Article(models.Model):
    article_title = models.CharField(max_length = 250)
    description = models.CharField(max_length = 250)
    author = models.CharField(max_length = 250)
    content = models.TextField()
    date_published = models.TimeField()

    def __str__(self):
        return self.article_title + ' - ' + self.description