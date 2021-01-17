# Generated by Django 3.1.4 on 2021-01-12 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kids', '0008_delete_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardigan',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='cardigan'),
        ),
        migrations.AddField(
            model_name='pullover',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='pullover'),
        ),
        migrations.AddField(
            model_name='vest',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='vest'),
        ),
    ]
