from datetime import date

from django.shortcuts import render
from django.core.paginator import Paginator

from books.converters import PubDateConverter
from books.models import Book


def books_view(request):
    books = Book.objects.all()
    template = 'books/books_list.html'
    context = {
        'books': books,
    }
    return render(request, template, context)


def book_view(request, pub_date):
    book = Book.objects.filter(pub_date=pub_date)
    prev_data = Book.objects.order_by('-pub_date').filter(pub_date__lt=pub_date).first()
    next_data = Book.objects.order_by('pub_date').filter(pub_date__gt=pub_date).first()
    template = 'books/books_list.html'
    context = {
        'book': book,
        'prev': prev_data,
        'next': next_data,
    }
    return render(request, template, context)
