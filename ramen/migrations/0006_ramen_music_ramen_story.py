# Generated by Django 4.2.7 on 2024-01-25 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ramen', '0005_ramen_company_ramen_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='ramen',
            name='music',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ramen',
            name='story',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
