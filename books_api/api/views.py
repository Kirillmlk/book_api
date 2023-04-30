from rest_framework import viewsets, permissions
from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.select_related('author')
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = BookSerializer
