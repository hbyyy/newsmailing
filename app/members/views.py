from django.contrib.auth import get_user_model
# Create your views here.
from django.views.generic import FormView

from members.forms import SignupForm

User = get_user_model()


class Index(FormView):
    template_name = 'index.html'
    form_class = SignupForm
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)


def email_auth(request, token):
    if request.method == 'GET':
        try:
            user = User.objects.get(token=token)
            user.is_active = True
            user.save()

        except User.DoesNotExist():
            pass
