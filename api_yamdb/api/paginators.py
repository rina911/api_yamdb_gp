from rest_framework.pagination import PageNumberPagination


class ReviewPagination(PageNumberPagination):
    """Пагинатор для отзывов."""

    page_size = 4


class CommentPagination(PageNumberPagination):
    """Пагинатор для комментариев."""

    page_size = 4
