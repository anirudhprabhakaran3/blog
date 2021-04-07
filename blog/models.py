from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):

    DESCRIPTIONS = 'DR'
    NATURE = 'NA'
    THRESHOLD = 'TH'
    EXP = 'E'
    SCHOOL = 'SC'

    CAT_CHOICES = [
    (DESCRIPTIONS, 'Descriptions'),
    (NATURE, 'Nature'),
    (THRESHOLD, 'Threshold'),
    (EXP, 'Experiences'),
    (SCHOOL, 'School')
    ]

    author = models.CharField(max_length=200, default="Anirudh Prabhakaran")
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=300, default="https://picsum.photos/700?random=10")
    category = models.CharField(
    max_length=2,
    choices=CAT_CHOICES,
    default=SCHOOL
    )
    content = models.TextField()
    batch = models.IntegerField()
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title

class Message(models.Model):

    Alert = 'AL'
    Information = 'IF'

    TYPE = [
    (Alert, 'Alert'),
    (Information, 'Information')
    ]

    subject = models.CharField(max_length=100, blank=True)
    type = models.CharField(
    max_length=2,
    choices = TYPE,
    default = Information,
    )
    content = models.TextField()
    def __str__(self):
        return self.subject
