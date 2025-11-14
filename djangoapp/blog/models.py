from django.db import models
from utils.slug_creator import create_slug


class Tag(models.Model):
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    name = models.CharField(max_length=50)
    slug = models.SlugField(
        unique=True,
        default=None,
        null=True, blank=True,
        max_length=100,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = create_slug(self.name, 3)
        return super().save(*args, **kwargs)


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=50)
    slug = models.SlugField(
        unique=True,
        default=None,
        null=True, blank=True,
        max_length=100,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = create_slug(self.name, 3)
        return super().save(*args, **kwargs)
