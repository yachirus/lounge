import os.path
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Lounge(models.Model):
    name = models.CharField(max_length = 256)
    editors = models.ManyToManyField(User, related_name = 'lounges_belongs_to_as_editor')
    members = models.ManyToManyField(User, related_name = 'lounges_belongs_to')

class CommentBase(models.Model):
    posted_by = models.ForeignKey(User)
    date_time = models.DateTimeField(auto_now = True)
    content = models.TextField()
    class Meta:
        abstract = True

class Topic(CommentBase):
    ACCESS_RIGHTS_CHOICES = (
        ('P', 'Public'),
        ('M', 'Member only'),
        ('E', 'Editor only'),
        ('C', 'Custom'),
    )
    lounge_belongs_to = models.ForeignKey('Lounge')
    tags = models.ManyToManyField('Tag', related_name = 'topics', blank=True)
    access_rights = models.CharField(max_length = 1, choices = ACCESS_RIGHTS_CHOICES)
    title = models.CharField(max_length = 256)

class Comment(CommentBase):
    topic = models.ForeignKey('Topic')

class Tag(models.Model):
    tag_name = models.CharField(max_length = 256)

class UserProfile(models.Model):
    def upload_to(instance, filename):
        return os.path.join('UserProfile', instance.user.username, filename)
    
    user = models.ForeignKey(User, unique=True)
    photo = models.ImageField(upload_to = upload_to, blank=True)
    settings = models.TextField(blank=True)