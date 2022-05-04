from email.mime import image
from turtle import title
from django.db import models

# Create your models here.

class Author(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.fname} {self.lname}"

class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'image')
    date = models.DateField()
    slug = models.SlugField()
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"
    
class CommentModel(models.Model):
    user_name = models.CharField(max_length=50, blank=False)
    text = models.TextField(max_length=400, blank=False)
    post = models.ForeignKey(BlogModel, on_delete=models.CASCADE)
    # post = models.ForeignKey(BlogModel, on_delete=models.CASCADE, related_name='commets')

