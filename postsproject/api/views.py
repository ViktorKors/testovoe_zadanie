from typing import Any

from drf_yasg.utils import swagger_auto_schema
from rest_framework import filters, status, viewsets
from rest_framework.response import Response

from posts.models import Post

from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    ViewSet для работы с моделью Post.
    """

    queryset: Any = Post.objects.all()
    serializer_class: Any = PostSerializer
    filter_backends: list = [filters.SearchFilter]
    search_fields: list = ["title", "content"]

    @swagger_auto_schema(auto_schema=None)
    def partial_update(
        self, request: Any, *args: Any, **kwargs: Any
    ) -> Response:
        """
        Возвращает ответ о недопустимости метода с кодом состояния 405.
        """
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
