# Generated by Django 4.2.2 on 2023-06-20 05:59

import backend.models
from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('email',), 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Список пользователей'},
        ),
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', backend.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='company',
            field=models.CharField(blank=True, max_length=40, verbose_name='Компания'),
        ),
        migrations.AddField(
            model_name='user',
            name='position',
            field=models.CharField(blank=True, max_length=40, verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('seller', 'Продавец'), ('client', 'Клиент(Покупатель)')], default='buyer', max_length=50, verbose_name='Тип пользователя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
        migrations.CreateModel(
            name='ConfirmEmailToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='When was this token generated')),
                ('key', models.CharField(db_index=True, max_length=64, unique=True, verbose_name='Key')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='confirm_email_tokens', to=settings.AUTH_USER_MODEL, verbose_name='The User which is associated to this password reset token')),
            ],
            options={
                'verbose_name': 'Токен подтверждения Email',
                'verbose_name_plural': 'Токены подтверждения Email',
            },
        ),
    ]
