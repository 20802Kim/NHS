# Generated by Django 5.0.7 on 2024-08-13 00:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NHSApp', '0006_post_views'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='downvote',
        ),
        migrations.RemoveField(
            model_name='post',
            name='upvote',
        ),
        migrations.AddField(
            model_name='post',
            name='downvote',
            field=models.ManyToManyField(blank=True, related_name='downvoted_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='upvote',
            field=models.ManyToManyField(blank=True, related_name='upvoted_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
