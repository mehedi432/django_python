# Generated by Django 3.1.4 on 2021-01-12 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kids', '0009_auto_20210112_0332'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='category'),
        ),
    ]
