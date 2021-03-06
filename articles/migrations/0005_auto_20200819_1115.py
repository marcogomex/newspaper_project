# Generated by Django 3.0.8 on 2020-08-19 11:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20200724_1303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(default='None'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(max_length=100),
        ),
    ]
