from django.contrib.auth import get_user_model
from django.shortcuts import render
# Create your views here.
from django.views.generic import FormView

from members.forms import SubscribeForm

User = get_user_model()


def testview(request):
    return render(request, 'index.html')


class Index(FormView):
    template_name = 'index.html'
    form_class = SubscribeForm
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid()


def email_auth(request, token):
    if request.method == 'GET':
        try:
            user = User.objects.get(token=token)
            user.is_active = True
            user.save()

        except User.DoesNotExist():
            pass
