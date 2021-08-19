from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length = 15, unique=True)
    slug = models.SlugField(max_length = 15, unique = True)
    description = models.TextField(max_length = 255, blank = True)
    grid_size = models.CharField(max_length=20, blank = True)
    cat_image = models.ImageField(upload_to = 'photos/categories', blank = True)

    class Meta():
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__ (self):
        return self.category_name
