# Generated by Django 3.1.1 on 2020-09-26 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('subject_Name', models.CharField(max_length=40)),
                ('qualification', models.CharField(max_length=100)),
            ],
        ),
    ]
