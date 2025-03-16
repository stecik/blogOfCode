from django.urls import path
from .views import ArticlesListCreate, ArticleRetrieveUpdateDestroy

urlpatterns = [
    path("articles/", ArticlesListCreate.as_view(), name="articles"),
    path("articles/<int:pk>/", ArticleRetrieveUpdateDestroy.as_view(), name="article"),
]
