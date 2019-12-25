from django.db import models

# Create your models here.

class News(models.Model):

    title = models.CharField('Title',max_length=255)
    content = models.TextField('Content')
    author = models.CharField(max_length=55)
    image = models.ImageField(upload_to='news_images',null=True,blank=True)

    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return f'{self.title} {self.author} {self.created_at}'
