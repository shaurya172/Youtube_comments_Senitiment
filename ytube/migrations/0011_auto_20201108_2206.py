# Generated by Django 3.1.2 on 2020-11-08 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ytube', '0010_auto_20201108_2002'),
    ]

    operations = [
        migrations.RenameField(
            model_name='output_sent',
            old_name='Op_Text',
            new_name='op_text',
        ),
    ]
