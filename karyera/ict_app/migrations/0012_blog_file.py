# Generated by Django 2.2.7 on 2020-01-29 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ict_app', '0011_contactpart'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='blog_files'),
        ),
    ]