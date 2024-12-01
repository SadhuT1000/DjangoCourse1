from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from mailing.models import ReceiveMail, Message, Mailing, AttemptMailing
from django.urls import reverse_lazy, reverse
from .forms import (MailingForm, MessageForm, ReceiveMailModeratorForm,
                    MailingModeratorForm, ReceiveMailModeratorForm, ReceiveMailForm)



def base(request):

    return render(request, "base.html")


# Главная страница
class homeView(TemplateView):
    template_name = 'mailing/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mail_count"] = len(Mailing.objects.all())
        context["active_count"] = len(Mailing.objects.filter(status="Запущен"))
        context["unique_email"] = len(Mailing.objects.all())
        return context


# Шаблон контакты
class Contacts(TemplateView):


    template_name = "mailing/contacts.html"

    def contacts(request):
        if request.method == "POST":
            name = request.POST.get("name")  # получаем имя
            message = request.POST.get("message")  # получаем сообщение
            return HttpResponse(f"Спасибо, {name}! {message} Сообщение получено.")
        return render(request, "mailing/contacts.html")


# Страница ответа на отправленное сообщение
class Message(TemplateView):

    template_name = "mailing/message.html"


# CRUD для рассылок
class MailingListView(ListView):
    model = Mailing

class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')


class MailingDetailView(LoginRequiredMixin, DetailView):
    model = Mailing
    form_class = MailingForm


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')

    def get_form_class(self):
        user = self.request.user
        if user.has_perm('mailing.set_is_active'):
            return MailingModeratorForm
        return MailingForm



class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing:mailing_list')

# CRUD для получателей

class ReceiveMailListView(ListView):
    model = ReceiveMail


class ReceiveMailDetailView(LoginRequiredMixin, DetailView):
    model = ReceiveMail
    form_class = ReceiveMailModeratorForm

class ReceiveMailCreateView(LoginRequiredMixin, CreateView):
    model = ReceiveMail
    form_class = ReceiveMailModeratorForm
    success_url = reverse_lazy('mailing:receive_list')


class ReceiveMailUpdateView(LoginRequiredMixin, UpdateView):
    model = ReceiveMail
    form_class = ReceiveMailForm
    success_url = reverse_lazy('mailing:receive_list')

    def get_form_class(self):
        user = self.request.user
        if user.has_perm('mailing.can_blocking_client'):
            return ReceiveMailModeratorForm
        return ReceiveMailForm



class ReceiveMailingDeleteView(LoginRequiredMixin, DeleteView):
    model = ReceiveMail
    success_url = reverse_lazy('mailing:receive_list')


# CRUD для сообщений
class MessageListView(ListView):
    model = Message


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message
    form_class = MessageForm


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')





class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('mailing:message_list')



class MailingAttemptCreateView(LoginRequiredMixin, CreateView):
    model = AttemptMailing

    def form_valid(self, form):
        recipient = form.save()
        recipient.owner = self.request.user
        recipient.save()
        return super().form_valid(form)


class MailingAttemptListView(LoginRequiredMixin, ListView):
    model = AttemptMailing

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_superuser:
            return super().get_queryset()
        elif self.request.user.groups.filter(name="Пользователи").exists():
            return super().get_queryset().filter(owner=self.request.user)
        raise PermissionDenied

