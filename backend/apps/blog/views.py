from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .permissions import IsAuthorOrStaff
from .serializers import ArticleSerializer, CategorySerializer
from .models import Article, Category


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


class CategoryListCreate(generics.ListCreateAPIView):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        if self.request.method == "POST":
            return [IsAdminUser()]

        return super().get_permissions()


class CategoryRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [IsAdminUser()]

        return super().get_permissions()
