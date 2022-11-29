from django.db import models
from news.models import Profile
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=250)
    # content = models.TextField()
    content = RichTextField(blank=True, null=True)
    author = models.ForeignKey(Profile,  on_delete=models.CASCADE, related_name="blog_posts")
    published = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-published']

    def __str__(self):
        return self.title