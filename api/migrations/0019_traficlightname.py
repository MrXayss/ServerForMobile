# Generated by Django 3.1.5 on 2022-04-15 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_infotrafficlight_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='TraficLightName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_trafficlight', models.CharField(default='0', max_length=100, verbose_name='Название перекрестка')),
            ],
        ),
    ]
