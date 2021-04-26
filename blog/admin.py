from django.contrib import admin
from .models import Post, Message, Category

admin.site.register(Post)
admin.site.register(Message)
admin.site.register(Category)
admin.site.site_header = 'BLOG CMS'
