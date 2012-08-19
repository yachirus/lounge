from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Lounge(models.Model):
    name = models.CharField(max_length = 256)
    editors = models.ManyToManyField(User, related_name = 'lounges_belongs_to_as_editor')
    members = models.ManyToManyField(User, related_name = 'lounges_belongs_to')

class Topic(models.Model):
    posted_by = models.ForeignKey(User)
    date_time = models.DateTimeField(auto_now = True)
    lounge_belongs_to = models.ForeignKey('Lounge')
    tags = models.ManyToManyField('Tag', related_name = 'topics')
    title = models.CharField(max_length = 256)
    content = models.TextField()

class Comment(models.Model):
    content = models.TextField()

class Tag(models.Model):
    tag_name = models.CharField(max_length = 256)