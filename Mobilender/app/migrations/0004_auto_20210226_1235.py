# Generated by Django 2.2.19 on 2021-02-26 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210225_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='code',
            field=models.IntegerField(),
        ),
    ]