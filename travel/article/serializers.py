from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):

	class Meta:
		model = Article
		fields = ('article_title', 'description')

		# If all field are required
		# fields = '__all__'

