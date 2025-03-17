from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Article, Tag, Category

CustomUser = get_user_model()


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ["name"]


class ArticleSerializer(serializers.ModelSerializer):

    tags = serializers.ListField(child=serializers.CharField(), write_only=True)
    tags_display = serializers.SerializerMethodField()
    authors = serializers.ListField(child=serializers.IntegerField(), write_only=True)
    authors_display = serializers.SerializerMethodField()
    categories = serializers.ListField(
        child=serializers.IntegerField(), write_only=True
    )
    categories_display = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = [
            "id",
            "title",
            "content",
            "authors",
            "authors_display",
            "created_at",
            "updated_at",
            "tags",
            "tags_display",
            "categories",
            "categories_display",
        ]

    def create(self, validated_data):
        tags = validated_data.pop("tags", [])
        authors = validated_data.pop("authors", [])
        categories = validated_data.pop("categories", [])

        article = Article.objects.create(**validated_data)
        article.authors.set(CustomUser.objects.filter(id__in=authors))
        article.categories.set(Category.objects.filter(id__in=categories))

        for tag in tags:
            tag_obj, _ = Tag.objects.get_or_create(name=tag)
            article.tags.add(tag_obj)

        return article

    def get_tags_display(self, obj):
        return [tag.name for tag in obj.tags.all()]

    def get_authors_display(self, obj):
        return [author.username for author in obj.authors.all()]

    def get_categories_display(self, obj):
        return [category.name for category in obj.categories.all()]


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["name"]
