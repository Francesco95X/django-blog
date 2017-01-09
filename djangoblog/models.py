from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager

# Blog models

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    image = models.FileField(null=True, blank=True)
    text = models.TextField()
    tags = TaggableManager()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

# For python2 use __unicode__ instead
    def __str__(self):
        return self.title

# Comment system

class Comment(models.Model):
    post = models.ForeignKey('djangoblog.Post', related_name='comments')
    name = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
