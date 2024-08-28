from django.urls import path

from books import views


urlpatterns = [
    path("", views.BookListView.as_view(), name="book_list"),
    path("<uuid:pk>/", views.BookDetailView.as_view(), name="book_detail"),
    path("<uuid:book_id>/add-review", views.ReviewCreateFormView.as_view(), name="book-review-add"),
    path("search/", views.SearchResultsListView.as_view(), name="search_results"),
]
