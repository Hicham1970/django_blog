from django.db import models
from django.utils import timezone

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length= 2025)
    content = models.TextField()
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)
    likes = models.PositiveIntegerField(default=0)



    # def publish(self):
    #     self.published_at = timezone.now()
    #     self.save()

    def __str__(self):
        return self.title



class Comment(models.Model):
    posts = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=300)
    email = models.EmailField()
    body = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Comment by {self.author} on {self.blog}'

   