# Generated by Django 3.1.2 on 2020-11-08 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ytube', '0007_auto_20201108_1947'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='output_sent',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='sentiment',
            options={'managed': True},
        ),
        migrations.AlterModelTable(
            name='output_sent',
            table='Table2',
        ),
        migrations.AlterModelTable(
            name='sentiment',
            table='Table1',
        ),
    ]
