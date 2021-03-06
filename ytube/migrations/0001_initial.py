# Generated by Django 3.1.2 on 2020-10-27 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('population', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'myapp_city',
            },
        ),
        migrations.CreateModel(
            name='sentiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_sentiment', models.CharField(max_length=500)),
            ],
        ),
    ]
