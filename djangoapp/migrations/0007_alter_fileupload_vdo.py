# Generated by Django 4.2.4 on 2023-08-23 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0006_fileupload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='vdo',
            field=models.FileField(upload_to='djangoapp/static'),
        ),
    ]