from django.urls import path

from books.views import BookListView
from books.views import BookDetailView
from books.views import SearchResultsListView

urlpatterns = [
    path("", BookListView.as_view(), name="book_list"),
    path("<uuid:pk>/", BookDetailView.as_view(), name="book_detail"),
    path("search/", SearchResultsListView.as_view(), name="search_results"),
]
