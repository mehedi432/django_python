# Generated by Django 3.1.4 on 2021-01-11 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kids', '0003_gender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cardigan',
            old_name='name',
            new_name='category',
        ),
    ]