# Generated by Django 3.1.2 on 2020-10-28 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ytube', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('profit', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='City',
        ),
    ]
