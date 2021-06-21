from django.db import models
from django.utils import timezone
from django.urls import reverse

from tinymce.models import HTMLField

# Create your models here.

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=300, default="https://picsum.photos/700?random=10")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('categories_detail', kwargs={'pk': self.pk})

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=300, default="https://picsum.photos/700?random=10")
    image_credits = models.CharField(max_length=200, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(max_length=200, blank=True, null=True)
    content = HTMLField()
    created_date = models.DateField(default=timezone.now)
    published_date = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['-id']

    def get_absolute_url(self):
        return reverse('test_slug', kwargs={'slug' : self.slug})

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Message(models.Model):

    Alert = 'AL'
    Information = 'IF'

    TYPE = [
    (Alert, 'Alert'),
    (Information, 'Information')
    ]
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=100, blank=True)
    type = models.CharField(
    max_length=2,
    choices = TYPE,
    default = Information,
    )
    content = models.TextField()
    def __str__(self):
        return self.subject
