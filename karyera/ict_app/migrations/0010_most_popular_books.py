# Generated by Django 2.2.7 on 2020-01-28 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ict_app', '0009_auto_20200120_1929'),
    ]

    operations = [
        migrations.CreateModel(
            name='Most_popular_books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
    ]