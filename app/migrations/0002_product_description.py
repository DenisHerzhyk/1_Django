# Generated by Django 4.2 on 2023-07-23 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
    ]