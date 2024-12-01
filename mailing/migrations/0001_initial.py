# Generated by Django 5.1.2 on 2024-11-09 07:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_sending', models.DateTimeField(verbose_name='Дата первой отправки')),
                ('end_sending', models.DateTimeField(verbose_name='Дата окончания отправки')),
                ('status', models.CharField(choices=[('Создано', 'Создано'), ('Запущено', 'Запущено'), ('Завершена', 'Завершена')], default='Создано', max_length=11, verbose_name='Статус рассылки')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
                'ordering': ['first_sending'],
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255, verbose_name='Тема письма')),
                ('content', models.TextField(verbose_name='Содержимое письма')),
            ],
            options={
                'verbose_name': 'письмо',
                'verbose_name_plural': 'письма',
                'ordering': ['subject'],
            },
        ),
        migrations.CreateModel(
            name='ReceiveMail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.EmailField(max_length=255, unique=True, verbose_name='Письмо')),
                ('fio', models.CharField(max_length=255, verbose_name='ФИО')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарии')),
            ],
            options={
                'verbose_name': 'получатель',
                'verbose_name_plural': 'получатели',
                'ordering': ['fio'],
            },
        ),
        migrations.CreateModel(
            name='AttemptMailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_attempt', models.DateTimeField(verbose_name='Дата и время попытки')),
                ('status', models.CharField(max_length=115, verbose_name='Статус попытки')),
                ('response', models.TextField(blank=True, null=True, verbose_name='Комментарии')),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mailing', to='mailing.mailing', verbose_name='Рассылка')),
            ],
            options={
                'verbose_name': 'попытка',
                'verbose_name_plural': 'попытки',
                'ordering': ['date_attempt', 'status'],
            },
        ),
        migrations.AddField(
            model_name='mailing',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mailings', to='mailing.message', verbose_name='Сообщение'),
        ),
        migrations.AddField(
            model_name='mailing',
            name='client',
            field=models.ManyToManyField(to='mailing.receivemail', verbose_name='Клиент'),
        ),
    ]
