# Generated by Django 2.2.19 on 2021-02-27 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210227_0810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]