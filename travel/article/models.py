from django.db import models

# Create your models here.
class Tags(models.Model):
	label = models.CharField(max_length = 30)

	def __str__(self):
		return self.label

class Article(models.Model):
    article_title = models.CharField(max_length = 250)
    description = models.TextField()
    content = models.TextField()
    author = models.CharField(max_length = 250)
    date_published = models.DateTimeField(auto_now=True)
    # thumbnail = models.ImageField(upload_to = 'media/' , default = 'media/travel1.jpg')
    # header = models.ImageField(upload_to = 'media/', default = 'media/travel1.jpg')

    def __str__(self):
        return self.article_title + ' - ' + self.description