# Generated by Django 4.2 on 2023-04-13 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_course_coursedescription'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='video',
            field=models.FileField(null=True, upload_to='video/%y'),
        ),
    ]