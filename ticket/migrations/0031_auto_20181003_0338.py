# Generated by Django 2.1.1 on 2018-10-03 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0030_remove_vodtepschetchic_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schetchic',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Цена'),
        ),
    ]
