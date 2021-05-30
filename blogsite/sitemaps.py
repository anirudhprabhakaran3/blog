from django.contrib.sitemaps import Sitemap
from django.contrib.sites.models import Site
from django.urls import reverse

from blog.models import Post, Category

class StaticSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return ['about', 'search']
    
    def location(self, item):
        return reverse(item)

class PostSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return Post.objects.all()

class CategorySitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return Category.objects.all()