from django.db import models

from postsproject.constants import (
    MAX_CONTENT_LENGTH,
    MAX_CONTENT_PREVIEW_LENGTH,
    MAX_TITLE_LENGTH,
)


class Post(models.Model):
    """
    Модель постов.
    """

    title = models.CharField(
        max_length=MAX_TITLE_LENGTH, verbose_name="Заголовок"
    )
    content = models.TextField(
        max_length=MAX_CONTENT_LENGTH, verbose_name="Содержимое"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата обновления"
    )

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return (
            f"{self.title} - {self.content[:MAX_CONTENT_PREVIEW_LENGTH]}"
            if len(self.content) > MAX_CONTENT_PREVIEW_LENGTH
            else f"{self.title} - {self.content}"
        )
