from django.contrib import admin
from .models import Forum
from .models import ListForum

# Register your models here.
admin.site.register(Forum)
admin.site.register(ListForum)