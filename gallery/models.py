from django.db import models


class Photo(models.Model):
    """Modelio klasės galerija"""
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='gallery')
    captions = models.TextField(blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Gallery(models.Model):
    """Modelio galerija"""
    name = models.CharField(max_length=250)
    images = models.ManyToManyField(Photo)
    captions = models.TextField(max_length=250, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']