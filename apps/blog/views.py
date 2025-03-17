from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsAuthorOrStaff
from .serializers import ArticleSerializer
from .models import Article


class ArticlesListCreate(generics.ListCreateAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        if self.request.method == "POST":
            return [IsAuthenticated()]
        return super().get_permissions()


class ArticleRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        if self.request.method in ["PUT", "PATCH", "DELETE"]:

            return [IsAuthenticated(), IsAuthorOrStaff()]
        return super().get_permissions()
