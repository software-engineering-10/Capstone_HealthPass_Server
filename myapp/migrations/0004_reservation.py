# Generated by Django 4.2.5 on 2023-10-04 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_account_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=20)),
                ('time', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('seat', models.CharField(max_length=20)),
                ('ex_name', models.CharField(max_length=20)),
                ('user_name', models.CharField(max_length=20)),
                ('user_phone', models.CharField(max_length=20)),
            ],
        ),
    ]
