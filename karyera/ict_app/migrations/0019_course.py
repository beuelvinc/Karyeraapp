# Generated by Django 2.2.7 on 2020-01-31 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ict_app', '0018_auto_20200131_1209'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('course_link', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='course_images')),
            ],
        ),
    ]
