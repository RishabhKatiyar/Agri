# Generated by Django 3.2.4 on 2021-06-12 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.TextField(max_length=50)),
                ('content', models.TextField(max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
