# Generated by Django 3.1.7 on 2021-03-07 17:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_equipments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notebooks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(choices=[('', '브랜드 선택'), ('gram', 'gram'), ('ultra', 'ultra'), ('samsung', 'samsung'), ('asus', 'asus'), ('hansung', 'hansung')], default='', max_length=20)),
                ('cpu', models.CharField(blank=True, max_length=50)),
                ('ram', models.CharField(blank=True, max_length=50)),
                ('drive', models.CharField(blank=True, max_length=50)),
                ('gpu', models.CharField(blank=True, max_length=50)),
                ('purchase_date', models.DateField(blank=True, default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
                ('rank', models.CharField(choices=[('', '직급 선택'), ('S3', 'S3'), ('S4', 'S4'), ('S5', 'S5'), ('S6', 'S6'), ('S7', 'S7'), ('S8', 'S8'), ('Freelancer', 'Freelancer'), ('Intern', 'Intern'), ('Contract', 'Contract')], default='', max_length=20)),
                ('seat', models.IntegerField(blank=True, default=1)),
            ],
        ),
        migrations.AlterField(
            model_name='equipment',
            name='rank',
            field=models.CharField(choices=[('', '직급 선택'), ('S3', 'S3'), ('S4', 'S4'), ('S5', 'S5'), ('S6', 'S6'), ('S7', 'S7'), ('S8', 'S8'), ('Freelancer', 'Freelancer'), ('Intern', 'Intern'), ('Contract', 'Contract')], default='Not Ranked', max_length=20),
        ),
    ]