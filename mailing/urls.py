
from mailing.apps import MailingConfig
from django.urls import path, include
from mailing.views import home

app_name = MailingConfig.name

urlpatterns = [
    path('', home, name='home'),
]
