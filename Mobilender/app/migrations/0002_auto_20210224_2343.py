# Generated by Django 2.2.19 on 2021-02-25 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='type_customer',
            field=models.CharField(choices=[('NORMAL', 'Normal'), ('PLATA', 'Plata'), ('ORO', 'Oro'), ('PLATINO', 'Platino')], default='NORMAL', max_length=10),
        ),
    ]