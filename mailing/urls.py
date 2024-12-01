
from mailing.apps import MailingConfig
from django.urls import path, include
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


    path('mailing/', MailingListView.as_view(), name='mailing_list'),
    path('mailing/<int:pk>/detail/', MailingDetailView.as_view(), name='mailing_detail'),
    path('mailing/new/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailing/<int:pk>/edit/', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailing/<int:pk>/delete/', MailingDeleteView.as_view(), name='mailing_delete'),


    path ('receive/', ReceiveMailListView.as_view(), name='receive_list'),
    path('receive/<int:pk>/detail/', ReceiveMailDetailView.as_view(), name='receive_detail'),
    path('receive/new/', ReceiveMailCreateView.as_view(), name='receive_create'),
    path('receive/<int:pk>/edit/', ReceiveMailUpdateView.as_view(), name='receive_update'),
    path('receive/<int:pk>/delete/', ReceiveMailingDeleteView.as_view(), name='receive_delete'),

    path ('message/', MessageListView.as_view(), name='message_list'),
    path('message/<int:pk>/detail/', MessageDetailView.as_view(), name='message_detail'),
    path('message/new/', MessageCreateView.as_view(), name='message_create'),
    path('message/<int:pk>/edit/', MessageUpdateView.as_view(), name='message_update'),
    path('message/<int:pk>/delete/', MessageDeleteView.as_view(), name='message_delete'),

    path("send/", MailingAttemptListView.as_view(), name="send_list"),
    path("send/create/", MailingAttemptCreateView.as_view(), name="send_create"),
]

