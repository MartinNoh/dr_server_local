# Generated by Django 3.1.7 on 2021-03-08 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_equipments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]