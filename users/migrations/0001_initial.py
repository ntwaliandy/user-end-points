# Generated by Django 3.0.5 on 2022-02-21 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDeatils',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('phone_number', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50000)),
            ],
        ),
    ]