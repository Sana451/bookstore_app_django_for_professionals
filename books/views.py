from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q, Prefetch
from django.views.generic import ListView, DetailView

from books.models import Book

User = get_user_model()


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "books/book_list.html"
    login_url = "account_login"


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Book
    context_object_name = "book"
    template_name = "books/book_detail.html"
    login_url = "account_login"
    permission_required = "books.special_status"
    queryset = Book.objects.prefetch_related(Prefetch("reviews__author", User.objects.all().only("username")))


class SearchResultsListView(ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "books/search_results.html"

    def get_queryset(self):
        search_query_from_form = self.request.GET.get("q")
        return Book.objects.filter(
            Q(title__icontains=search_query_from_form) | Q(author__icontains=search_query_from_form)
        )
