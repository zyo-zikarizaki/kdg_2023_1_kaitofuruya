# Generated by Django 4.2.7 on 2024-01-29 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ramen', '0022_legend_time_alter_review_rate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='legend',
            old_name='thumbnail',
            new_name='thumbnail_legend',
        ),
        migrations.AlterField(
            model_name='review',
            name='rate',
            field=models.IntegerField(choices=[(5, '5'), (3, '3'), (2, '2'), (4, '4'), (0, '0'), (1, '1')]),
        ),
    ]
