# Generated by Django 4.0.1 on 2022-01-21 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_user_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='slug',
        ),
    ]