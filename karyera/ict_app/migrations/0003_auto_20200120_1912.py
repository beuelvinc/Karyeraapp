# Generated by Django 2.2.7 on 2020-01-20 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ict_app', '0002_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
