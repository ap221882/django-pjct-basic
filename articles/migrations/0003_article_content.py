# Generated by Django 3.2.7 on 2021-09-07 10:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_remove_article_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
