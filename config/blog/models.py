from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 70)
    text = models.TextField()
    likes = models.IntegerField(blank=True,null=True)
    rating = models.FloatField(blank=True,null=True)
    created_at = models.DateTimeField(null=True)
    is_published = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images/', null=True )
