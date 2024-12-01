from django.views.decorators.cache import cache_page

from mailing.apps import MailingConfig
from django.urls import path, include

from mailing.services import send_email
from mailing.views import homeView, Contacts, Message
from mailing.views import (MailingCreateView, MailingDeleteView, MailingDetailView, MailingUpdateView,
                           MessageCreateView, MailingListView, MessageDeleteView, MessageDetailView,
                           MessageUpdateView, MessageListView, ReceiveMailListView, ReceiveMailCreateView,
                           ReceiveMailUpdateView, ReceiveMailDetailView, ReceiveMailingDeleteView, MailingAttemptListView, MailingAttemptCreateView)

app_name = MailingConfig.name

urlpatterns = [
    path('home/', homeView.as_view(), name='home'),
    path("contacts/", Contacts.as_view(), name="contacts"),
    path("message/", Message.as_view(), name="message"),


    path('mailing/', cache_page(60)(MailingListView.as_view()), name='mailing_list'),
    path('mailing/<int:pk>/detail/', cache_page(60)(MailingDetailView.as_view()), name='mailing_detail'),
    path('mailing/new/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailing/<int:pk>/edit/', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailing/<int:pk>/delete/', MailingDeleteView.as_view(), name='mailing_delete'),


    path ('receivemail/', cache_page(60)(ReceiveMailListView.as_view()), name='receivemail_list'),
    path('receivemail/<int:pk>/detail/', cache_page(60)(ReceiveMailDetailView.as_view()), name='receivemail_detail'),
    path('receivemail/create/', ReceiveMailCreateView.as_view(), name='receivemail_form'),
    path('receivemail/<int:pk>/edit/', ReceiveMailUpdateView.as_view(), name='receivemail_update'),
    path('receivemail/<int:pk>/delete/', ReceiveMailingDeleteView.as_view(), name='receivemail_delete'),

    path ('message/', cache_page(60)(MessageListView.as_view()), name='message_list'),
    path('message/<int:pk>/detail/', cache_page(60)(MessageDetailView.as_view()), name='message_detail'),
    path('message/new/', MessageCreateView.as_view(), name='message_create'),
    path('message/<int:pk>/edit/', MessageUpdateView.as_view(), name='message_update'),
    path('message/<int:pk>/delete/', MessageDeleteView.as_view(), name='message_delete'),

    path("send/", cache_page(60)(MailingAttemptListView.as_view()), name="send_list"),
    path("send/create/", MailingAttemptCreateView.as_view(), name="send_create"),
    path("send_mail/", send_email, name="send_mail")
]

