from django.urls import path

from members.views import email_auth

app_name = 'members'
urlpatterns = [
    path('activate/<str:token>/', email_auth, name='activate'),

]
