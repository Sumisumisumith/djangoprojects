from django.contrib import admin
from .models import BlogPost

#Django管理サイトにBlogPostを登録する
admin.site.register(BlogPost)