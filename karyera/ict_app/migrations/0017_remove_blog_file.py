# Generated by Django 2.2.7 on 2020-01-31 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ict_app', '0016_blog_rank'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='file',
        ),
    ]