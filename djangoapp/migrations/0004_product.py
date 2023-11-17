# Generated by Django 4.2.4 on 2023-08-22 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0003_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('brand', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('exp', models.DateField()),
                ('des', models.CharField(max_length=200)),
            ],
        ),
    ]
