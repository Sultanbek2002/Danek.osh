# Generated by Django 5.2 on 2025-04-19 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='image',
            field=models.ImageField(default='', upload_to='banner/'),
        ),
        migrations.AddField(
            model_name='banner',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
