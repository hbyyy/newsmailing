from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from django.views import View
from django.views.generic import FormView

from members.forms import SubscribeForm


def testview(request):
    return render(request, 'index.html')


class Index(FormView):
    template_name = 'index.html'
    form_class = SubscribeForm
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid()


def email_auth(request, token):
    return HttpResponse(f'hello world {token}')

