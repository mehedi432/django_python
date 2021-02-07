# Generated by Django 3.1.1 on 2021-02-06 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=89)),
                ('image', models.ImageField(default='default.jpg', upload_to='category')),
            ],
        ),
        migrations.CreateModel(
            name='Vest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.CharField(max_length=34)),
                ('description', models.CharField(max_length=144)),
                ('composition', models.CharField(max_length=89)),
                ('gauge', models.CharField(max_length=34)),
                ('size', models.CharField(max_length=13)),
                ('weight', models.CharField(max_length=34)),
                ('moq', models.CharField(max_length=21)),
                ('fob', models.CharField(max_length=21)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kids.category')),
            ],
        ),
        migrations.CreateModel(
            name='Pullover',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.CharField(max_length=34)),
                ('description', models.CharField(max_length=144)),
                ('composition', models.CharField(max_length=89)),
                ('gauge', models.CharField(max_length=34)),
                ('size', models.CharField(max_length=13)),
                ('weight', models.CharField(max_length=34)),
                ('moq', models.CharField(max_length=21)),
                ('fob', models.CharField(max_length=21)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kids.category')),
            ],
        ),
        migrations.CreateModel(
            name='Cardigan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.CharField(max_length=34)),
                ('description', models.CharField(max_length=144)),
                ('composition', models.CharField(max_length=89)),
                ('gauge', models.CharField(max_length=34)),
                ('size', models.CharField(max_length=13)),
                ('weight', models.CharField(max_length=34)),
                ('moq', models.CharField(max_length=21)),
                ('fob', models.CharField(max_length=21)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kids.category')),
            ],
        ),
    ]
