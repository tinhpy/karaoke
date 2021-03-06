# Generated by Django 3.0.6 on 2020-06-29 08:39

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeeklySchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField()),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='security_question',
        ),
        migrations.RemoveField(
            model_name='user',
            name='serurity_answer',
        ),
        migrations.AddField(
            model_name='schedule',
            name='workingTime',
            field=models.CharField(choices=[('morning', 'morning'), ('afternoon', 'afternoon'), ('evening', 'evening')], default='afternoon', max_length=31),
        ),
        migrations.AddField(
            model_name='user',
            name='salary',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='weekDay',
            field=models.CharField(choices=[('monday', 'monday'), ('tuesday', 'tuesday'), ('wednesday', 'wednesday'), ('thursday', 'thursday'), ('friday', 'friday'), ('saturday', 'saturday'), ('sunday', 'sunday')], default='tuesday', max_length=31),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('NA', 'N/A')], default='male', max_length=31),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('Staff', 'Staff')], default='Staff', max_length=31),
        ),
        migrations.CreateModel(
            name='WeeklySalary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weeklySalary', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weekly_salaries', to=settings.AUTH_USER_MODEL)),
                ('weeklySchedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weekly_salaries', to='accounts.WeeklySchedule')),
            ],
        ),
        migrations.AddField(
            model_name='schedule',
            name='weeklySchedule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='accounts.WeeklySchedule'),
        ),
    ]
