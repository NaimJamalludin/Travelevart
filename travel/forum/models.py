from django.db import models

# Create your models here.
class Forum(models.Model):
    forum_title = models.CharField(max_length = 250)
    content = models.TextField()

    def __str__(self):
        return self.forum_title