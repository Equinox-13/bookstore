from django.db.models import Q
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book

# Note:
# For class based views we use LoginRequiredMixin whereas,
# For function based views we use login_required() decorator


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'book_list'
    login_url = 'account_login'


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'
    login_url = 'account_login'
    permission_required = 'books.special_status'


class SearchResultsListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'

    # Basic filtering using QuerySet
    # queryset = Book.objects.filter(title__icontains='beginners')

    def get_queryset(self):
        """
        Filtering using Q objects
        """
        return Book.objects.filter(Q(title__icontains='beginners') |
            Q(title__icontains='api'))

