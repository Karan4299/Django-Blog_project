from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    creation_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def create(self):
        self.creation_date = timezone.now()
        self.save()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={'pk':self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post',on_delete=models.CASCADE,related_name='comments')
    author = models.CharField(max_length=300)
    text = models.TextField(max_length=400)
    create_date = models.DateTimeField(default=timezone.now)
    comment_approve = models.BooleanField(default=False)

    def create(self):
        self.creation_date = timezone.now()
        self.save()

    def approve(self):
        self.comment_approve = True
        self.save()

    def get_absolute_url(self):
        return reverse("blog_list")

    def __str__(self):
        return self.text