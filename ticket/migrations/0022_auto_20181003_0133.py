# Generated by Django 2.1.1 on 2018-10-03 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0021_auto_20181002_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='du',
            name='vodcategory',
            field=models.ManyToManyField(blank=True, to='ticket.VodTepSchetchic', verbose_name='Счетчик'),
        ),
    ]
