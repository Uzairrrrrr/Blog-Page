# Generated by Django 4.2.13 on 2024-06-22 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_slug_post_author_alter_post_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='first', max_length=200, unique=True),
        ),
    ]