# Generated by Django 3.1.2 on 2020-11-08 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ytube', '0004_delete_charts'),
    ]

    operations = [
        migrations.CreateModel(
            name='output_sent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('op_text', models.CharField(max_length=100)),
                ('Sentiment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ytube.sentiment')),
            ],
        ),
    ]
