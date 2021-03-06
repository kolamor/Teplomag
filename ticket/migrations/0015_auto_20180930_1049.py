# Generated by Django 2.1.1 on 2018-09-30 10:49

from django.db import migrations, models
import django.db.models.deletion
import ticket.models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0014_auto_20180929_2056'),
    ]

    operations = [
        migrations.CreateModel(
            name='Combinir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
                ('textop', models.TextField(blank=True, verbose_name='текст')),
                ('image', models.ImageField(blank=True, upload_to=ticket.models.generate_filename1)),
            ],
        ),
        migrations.CreateModel(
            name='TaxomKrylchat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
                ('textop', models.TextField(blank=True, verbose_name='текст')),
                ('image', models.ImageField(blank=True, upload_to=ticket.models.generate_filename1)),
            ],
        ),
        migrations.CreateModel(
            name='TaxomTurb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
                ('textop', models.TextField(blank=True, verbose_name='текст')),
                ('image', models.ImageField(blank=True, upload_to=ticket.models.generate_filename1)),
            ],
        ),
        migrations.CreateModel(
            name='Teploschetchiki',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
                ('textop', models.TextField(blank=True, verbose_name='текст')),
                ('image', models.ImageField(blank=True, upload_to=ticket.models.generate_filename1)),
            ],
        ),
        migrations.CreateModel(
            name='Vodoschetchiki',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
                ('textop', models.TextField(blank=True, verbose_name='текст')),
                ('image', models.ImageField(blank=True, upload_to=ticket.models.generate_filename1)),
            ],
        ),
        migrations.AddField(
            model_name='taxomturb',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ticket.Vodoschetchiki', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='taxomkrylchat',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ticket.Vodoschetchiki', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='combinir',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ticket.Vodoschetchiki', verbose_name='Категория'),
        ),
    ]
