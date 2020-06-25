# Create your views here.
from django.views.generic import ListView

from articles.models import Article


class TestArticleView(ListView):
    model = Article
    template_name = 'test/testview.html'
    context_object_name = 'articles'
    ordering = 'pub_company'
