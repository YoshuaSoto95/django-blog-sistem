import uuid
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=200)
    create_at = models.DateTimeField(default=timezone.now)

    def __str__(self): 
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)
    create_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    image_main = models.ImageField(default="")
    description = models.TextField(max_length=200)
    content = RichTextField()
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    create_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
