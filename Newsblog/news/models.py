from django.db import models
from django.utils import timezone

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    category=(
        ('politics','Politics'),
        ('technologies','Technologies'),
        ('sport','Sport'),
        ('finance','Finance'),
        ('culture','Culture'),
    )
    
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.CharField(max_length=250)
    body = models.TextField()
    categorys=models.CharField(max_length=12,choices=category,default='')
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)