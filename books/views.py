from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q, Prefetch
from django.views.generic import ListView, DetailView, FormView, CreateView
from django.urls import reverse_lazy

from books.forms import BookReviewAddForm
from books.models import Book, Review

User = get_user_model()


# class BookListView(LoginRequiredMixin, ListView):
class BookListView(ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "books/book_list.html"
    login_url = "account_login"


# class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
class BookDetailView(DetailView):
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


# class ReviewCreateFormView(LoginRequiredMixin, CreateView):
class ReviewCreateFormView(CreateView):
    model = Review
    template_name = "books/book_review_form.html"
    form_class = BookReviewAddForm

    def get_success_url(self):
        book_id = self.kwargs["book_id"]
        return reverse_lazy('book_detail', kwargs={"pk": book_id})

    def form_valid(self, form):
        review = form.save(commit=False)
        book_id = self.kwargs["book_id"]
        review.book = Book.objects.get(id=book_id)
        review.author = self.request.user
        review.save()
        return super().form_valid(form)
