# Generated by Django 4.2.2 on 2023-06-28 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Overtime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=255)),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('multiplier', models.FloatField(choices=[(1.5, '1.5'), (2.0, '2.0'), (2.5, '2.5'), (3.0, '3.0')], default=1.5)),
                ('hourly_rate', models.FloatField()),
            ],
        ),
    ]