# Generated by Django 4.2 on 2023-04-13 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_course_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos/'),
        ),
    ]
