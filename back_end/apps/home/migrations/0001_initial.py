# Generated by Django 2.1.2 on 2018-11-19 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Checkmarks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('value', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Checkmark',
                'verbose_name_plural': 'Checkmarks',
            },
        ),
    ]
