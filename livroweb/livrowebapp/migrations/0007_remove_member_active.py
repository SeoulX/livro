# Generated by Django 4.2.5 on 2023-11-27 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livrowebapp', '0006_member_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='active',
        ),
    ]
