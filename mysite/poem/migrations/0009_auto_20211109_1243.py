# Generated by Django 3.2.8 on 2021-11-09 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poem', '0008_auto_20211109_1237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poem',
            name='poeti',
        ),
        migrations.AlterField(
            model_name='poem',
            name='poet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='poem.poet'),
        ),
    ]