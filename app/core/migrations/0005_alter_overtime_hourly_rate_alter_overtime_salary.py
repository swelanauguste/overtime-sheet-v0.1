# Generated by Django 4.2.2 on 2023-06-28 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_overtime_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='overtime',
            name='hourly_rate',
            field=models.DecimalField(decimal_places=2, default=5.5, max_digits=10),
        ),
        migrations.AlterField(
            model_name='overtime',
            name='salary',
            field=models.DecimalField(decimal_places=2, default=1800, max_digits=10),
        ),
    ]
