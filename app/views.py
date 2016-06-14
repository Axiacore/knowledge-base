from django.views.generic import ListView
from django.views.generic import DetailView

from .models import Category
from .models import Article
from .forms import SearchForm


class HomeView(ListView):
    template_name = 'home.html'
    model = Category
    context_object_name = 'category_list'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['form'] = SearchForm()
        return context


class CategoryDefaultView(DetailView):
    template_name = 'category_view.html'
    model = Category
    context_object_name = 'category'


class ArticleDefaultView(DetailView):
    template_name = 'article_view.html'
    model = Article
    context_object_name = 'article'


class SearchView(ListView):
    template_name = 'search_view.html'
    model = Article
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        context['form'] = SearchForm()
        return context
