# Create your views here.
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from articles.models import Article


@method_decorator(login_required, name='dispatch')
class TestArticleView(ListView):
    model = Article
    template_name = 'test/testview.html'
    context_object_name = 'articles'
    ordering = 'pub_company'
