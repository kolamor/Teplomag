# Generated by Django 2.1.1 on 2018-09-29 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0010_auto_20180929_0013'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriceUslugi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
                ('service', models.TextField(verbose_name='услуга')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('summ', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
