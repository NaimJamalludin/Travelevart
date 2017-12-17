from django.contrib import admin
from .models import Forum
from .models import ListForum
from .models import Comment

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
	list_display = ('user', 'email', 'approved')
	
admin.site.register(Forum)
admin.site.register(ListForum)
admin.site.register(Comment)