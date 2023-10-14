# Generated by Django 4.2.5 on 2023-10-13 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('seen', models.BooleanField()),
            ],
        ),
    ]
