from django.db import models
from django.contrib.auth import get_user_model

CustomUser = get_user_model()


class Category(models.Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Tag(models.Model):
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Article(models.Model):
    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    title = models.CharField(max_length=120)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    authors = models.ManyToManyField(CustomUser, related_name="articles")
    tags = models.ManyToManyField(Tag, related_name="articles")
    categories = models.ManyToManyField(Category, related_name="articles")

    def __str__(self):
        return self.title
