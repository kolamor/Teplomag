# Generated by Django 2.1.1 on 2018-09-29 00:03

from django.db import migrations, models
import ticket.models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0008_indexprimary'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название')),
                ('texts', models.TextField(verbose_name='текст')),
                ('texts1', models.TextField(blank=True, verbose_name='текст1')),
                ('texts2', models.TextField(blank=True, verbose_name='текст2')),
                ('image', models.ImageField(upload_to=ticket.models.generate_filename)),
            ],
        ),
    ]