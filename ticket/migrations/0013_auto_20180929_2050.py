# Generated by Django 2.1.1 on 2018-09-29 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0012_auto_20180929_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priceuslugi',
            name='summ',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, verbose_name='сумма'),
        ),
        migrations.AlterField(
            model_name='priceuslugi',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='стоимость'),
        ),
    ]
