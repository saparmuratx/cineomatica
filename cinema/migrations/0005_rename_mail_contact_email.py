# Generated by Django 4.1.3 on 2022-12-09 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0004_rename_number_contact_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='mail',
            new_name='email',
        ),
    ]
