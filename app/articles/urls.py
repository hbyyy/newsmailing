from django.urls import path
from .views import TestArticleView

urlpatterns = [
    path('testview/', TestArticleView.as_view(), name='testview'),
]