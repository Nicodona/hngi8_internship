# Generated by Django 3.2.6 on 2021-08-17 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoresume', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='description',
            field=models.TextField(default='hellow world'),
        ),
        migrations.AddField(
            model_name='data',
            name='job_desc',
            field=models.TextField(default='yoo bro'),
        ),
    ]
