# Generated by Django 2.1.4 on 2019-01-03 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id_no', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('college_name', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
