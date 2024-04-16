# Generated by Django 4.2.7 on 2024-01-29 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ramen', '0012_future_alter_review_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='future',
            name='acter',
        ),
        migrations.RemoveField(
            model_name='future',
            name='company',
        ),
        migrations.RemoveField(
            model_name='future',
            name='music',
        ),
        migrations.RemoveField(
            model_name='future',
            name='staff',
        ),
        migrations.RemoveField(
            model_name='future',
            name='story',
        ),
        migrations.RemoveField(
            model_name='future',
            name='thumbnail',
        ),
        migrations.AlterField(
            model_name='review',
            name='rate',
            field=models.IntegerField(choices=[(3, '3'), (2, '2'), (0, '0'), (4, '4'), (5, '5'), (1, '1')]),
        ),
    ]
