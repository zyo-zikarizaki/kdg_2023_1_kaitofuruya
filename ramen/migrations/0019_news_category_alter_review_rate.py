# Generated by Django 4.2.7 on 2024-01-29 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ramen', '0018_news_time_alter_review_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='category',
            field=models.CharField(choices=[('news', 'ニュース'), ('colam', '特集')], default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='rate',
            field=models.IntegerField(choices=[(4, '4'), (3, '3'), (1, '1'), (5, '5'), (2, '2'), (0, '0')]),
        ),
    ]
