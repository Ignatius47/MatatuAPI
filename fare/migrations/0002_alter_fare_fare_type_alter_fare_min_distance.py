# Generated by Django 5.0.7 on 2024-12-06 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fare', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fare',
            name='fare_type',
            field=models.CharField(choices=[('M-pesa', 'M-pesa'), ('Cash', 'Cash'), ('Courage', 'Courage'), ('Kidney', 'Kidney'), ('Fists', 'Fists'), ('Sambaza', 'Sambaza'), ('Boxing', 'Boxing'), ('Wreso', 'Wreso')], max_length=10),
        ),
        migrations.AlterField(
            model_name='fare',
            name='min_distance',
            field=models.FloatField(default=0.0),
        ),
    ]