# Generated by Django 2.2 on 2019-12-21 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_article_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='language',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.TextField(default=''),
        ),
    ]