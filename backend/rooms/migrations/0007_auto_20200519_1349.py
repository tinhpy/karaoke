# Generated by Django 3.0.6 on 2020-05-19 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0006_remove_payment_totalhourspend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='checkOutDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
