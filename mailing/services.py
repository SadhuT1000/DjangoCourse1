from config.settings import CACHE_ENABLED
from mailing.models import Mailing, AttemptMailing
from django.core.cache import cache
from django.shortcuts import get_object_or_404, redirect
from django.core.mail import send_mail

from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmailForm


def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipients = form.cleaned_data['recipients'].split(',')

            # Отправка письма всем получателям
            send_mail(
                subject,
                message,
                'admin@example.com',
                recipients,
                fail_silently=False,
            )
            return HttpResponse("Рассылка отправлена!")
    else:
        form = EmailForm()

    return render(request, 'mailing/send_mail.html', {'form': form})

def get_mailing_from_cache():
    """Получение данных по рассылкам из кэша, если кэш пуст берем из БД."""

    if not CACHE_ENABLED:
            return Mailing.objects.all()
    key = 'mailing_list'
    cache_mail = cache.get(key)
    if cache_mail is not None:
        return cache_mail
    cache_mail = Mailing.objects.all()
    cache.set(cache_mail, key)
    return cache_mail



def get_attempt_from_cache():
    """Получение данных по попыткам  из кэша, если кэш пуст берем из БД."""

    if not CACHE_ENABLED:
            return AttemptMailing.objects.all()
    key = 'attempt_list'
    cache_attempt = cache.get(key)
    if cache_attempt is not None:
        return cache_attempt
    cache_mail = Mailing.objects.all()
    cache.set(cache_attempt, key)
    return cache_attempt