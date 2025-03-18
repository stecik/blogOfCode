from django.urls import path
from .views import (
    ArticlesListCreate,
    ArticleRetrieveUpdateDestroy,
    CategoryListCreate,
    CategoryRetrieveUpdateDelete,
)

urlpatterns = [
    path("articles/", ArticlesListCreate.as_view(), name="articles"),
    path("articles/<int:pk>/", ArticleRetrieveUpdateDestroy.as_view(), name="article"),
    path("categories/", CategoryListCreate.as_view(), name="categories"),
    path(
        "categories/<int:pk>/",
        CategoryRetrieveUpdateDelete.as_view(),
        name="category",
    ),
]
