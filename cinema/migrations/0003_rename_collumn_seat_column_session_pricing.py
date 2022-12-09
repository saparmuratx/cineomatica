# Generated by Django 4.1.3 on 2022-12-09 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seat',
            old_name='collumn',
            new_name='column',
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.movie')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.room')),
            ],
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('children', models.FloatField(default=0)),
                ('adult', models.FloatField(default=0)),
                ('student', models.FloatField(default=0)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cinema.session')),
            ],
        ),
    ]
