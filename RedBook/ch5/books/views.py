from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from books.models import Book, Author, Publisher

# Create your views here.

# TemplateView
class BooksModelView(TemplateView):
    template_name = "books/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_list"] = ["Book", "Author", "Publisher"]
        return context


# ListView
# 해당 테이블로부터 모든 레코드를 가져와 object_list라는 context variable 구성
# template file : (default) books/모델명 소문자_list.html
class BookList(ListView):
    model = Book


class AuthorList(ListView):
    model = Author


class PublisherList(ListView):
    model = Publisher


# DetailView
# 해당 테이블로부터 특정 레코드를 가져와 object라는 context variable 구성
# template file : (default) books/모델명 소문자_detail.html
class BookDetail(DetailView):
    model = Book
    # PK 값은 URLconf에서 넘겨받는데 이에 대한 처리는 DetailView generic view에서 알아서 해줌


class AuthorDetail(DetailView):
    model = Author


class PublisherDetail(DetailView):
    model = Publisher