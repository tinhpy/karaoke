# Generated by Django 3.0.6 on 2020-05-27 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0007_auto_20200519_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='rooms.Room'),
        ),
    ]
