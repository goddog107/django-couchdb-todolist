from django.db import models

# Create your models here.


class PostManager(models.Manager):
  use_in_migrations = True

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    posted_at = models.DateField()
    objects = PostManager()

    def __str__(self):
        return self.title
