import re

from rest_framework import serializers

from posts.models import Post
from postsproject.constants import (
    MAX_CONTENT_LENGTH,
    MAX_TITLE_LENGTH,
    MIN_CONTENT_LENGTH,
    MIN_TITLE_LENGTH,
)


def validate_title_length(value: str) -> None:
    """
    Проверяет минимальную и максимаьную длину заголовка.
    """
    if len(value) < MIN_TITLE_LENGTH:
        raise serializers.ValidationError(
            f"Заголовок должен быть не менее {MIN_TITLE_LENGTH} символов."
        )
    if len(value) > MAX_TITLE_LENGTH:
        raise serializers.ValidationError(
            f"Заголовок не должен превышать {MAX_TITLE_LENGTH} символов."
        )


def validate_special_characters(value: str) -> None:
    """
    Проверяет наличие специальных символов в заголовке.
    """
    if re.search('[@#$%^&*(),.":{}|<>]', value):
        raise serializers.ValidationError(
            "Заголовок не должен содержать специальные символы."
        )


def validate_unique_title(value: str) -> None:
    """
    Проверяет уникальность заголовка.
    """
    if Post.objects.filter(title=value).exists():
        raise serializers.ValidationError(
            "Пост с таким заголовком уже существует."
        )


def validate_content_length(value: str) -> None:
    """
    Проверяет минимальную и максимальную длину контента.
    """
    if len(value) < MIN_CONTENT_LENGTH:
        raise serializers.ValidationError(
            f"Содержимое должно быть не менее {MIN_CONTENT_LENGTH} символов."
        )
    if len(value) > MAX_CONTENT_LENGTH:
        raise serializers.ValidationError(
            f"Содержимое не должно превышать  {MAX_CONTENT_LENGTH} символов."
        )


class PostSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Post.

    Проверяет и сериализует данные для создания и обновления постов.
    Проверяет заголовок на минимальную длину,
    отсутствие специальных символов и уникальность.
    Проверяет содержимое на минимальную и максимальную длину.
    """

    class Meta:
        model = Post
        fields = "__all__"

    def validate_title(self, value: str) -> str:
        """
        Валидирует заголовок поста.
        """
        validate_title_length(value)
        validate_special_characters(value)
        validate_unique_title(value)
        return value

    def validate_content(self, value: str) -> str:
        """
        Валидирует содержимое поста.
        """
        validate_content_length(value)
        return value
