# Generated by Django 2.1.2 on 2018-10-22 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0032_tag'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='schetchic',
            options={'ordering': ['title'], 'verbose_name': 'Счетчик', 'verbose_name_plural': 'Счетчики'},
        ),
        migrations.AddField(
            model_name='schetchic',
            name='specifications',
            field=models.TextField(blank=True, verbose_name='характиристики'),
        ),
    ]
