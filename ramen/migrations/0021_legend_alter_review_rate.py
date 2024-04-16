# Generated by Django 4.2.7 on 2024-01-29 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ramen', '0020_alter_news_category_alter_review_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Legend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('staff', models.TextField()),
                ('story', models.TextField()),
                ('music', models.CharField(max_length=100)),
                ('acter', models.TextField()),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='review',
            name='rate',
            field=models.IntegerField(choices=[(3, '3'), (5, '5'), (4, '4'), (0, '0'), (2, '2'), (1, '1')]),
        ),
    ]
