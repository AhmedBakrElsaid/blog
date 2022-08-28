# Generated by Django 4.1 on 2022-08-27 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=5000, verbose_name='Content'),
        ),
    ]