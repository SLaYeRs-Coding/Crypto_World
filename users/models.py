from django.db import models

# Create your models here.
class News(models.Model):
    
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField()
    image = models.ImageField(upload_to='news/', blank=True)
    category = models.TextField(max_length=25)

    class Meta:
        """Meta definition for News."""
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title