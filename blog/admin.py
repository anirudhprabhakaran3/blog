from django.contrib import admin
from .models import Post, Message

admin.site.register(Post)
admin.site.register(Message)
admin.site.site_header = 'BLOG CMS'
