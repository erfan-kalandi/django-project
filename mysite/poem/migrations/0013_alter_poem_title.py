# Generated by Django 3.2.8 on 2021-11-11 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poem', '0012_alter_poem_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poem',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
