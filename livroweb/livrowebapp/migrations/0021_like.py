# Generated by Django 4.2.5 on 2023-12-03 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('livrowebapp', '0020_alter_comment_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='livrowebapp.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livrowebapp.member')),
            ],
        ),
    ]
