# Generated by Django 3.1.1 on 2020-09-26 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book2',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('book_Name', models.CharField(max_length=200)),
                ('author_Name', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('pub_date', models.DateField()),
                ('image', models.ImageField(default='', upload_to='book/images')),
            ],
        ),
    ]
