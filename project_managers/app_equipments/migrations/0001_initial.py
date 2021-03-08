# Generated by Django 3.1.7 on 2021-03-08 07:28

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('device_id', models.IntegerField(primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('', '장비타입 선택'), ('notebook', 'notebook'), ('desktop', 'desktop'), ('monitor', 'monitor'), ('keyboard', 'keyboard'), ('mouse', 'mouse'), ('ex_storage', 'ex_storage'), ('network_eq', 'network_eq'), ('sound_eq', 'sound_eq'), ('accessory', 'accessory'), ('etc', 'etc')], default='', max_length=20)),
                ('brand', models.CharField(choices=[('', '브랜드 선택'), ('notebook', (('samsung_itech', 'samsung_itech'), ('gram512', 'gram512'), ('gram256', 'gram256'), ('ultra', 'ultra'), ('asus', 'asus'), ('hansung', 'hansung'))), ('desktop', (('deep_learning', 'deep_learning'), ('offer_interface', 'offer_interface'), ('run_client_app', 'run_client_app'))), ('monitor', (('samsung_itech', 'samsung_itech'), ('samsung', 'samsung'), ('lg', 'lg'), ('viewsync', 'viewsync'))), ('keyboard/mouse', (('samsung_itech', 'samsung_itech'), ('gram', 'gram'), ('ultra', 'ultra'), ('logitech', 'logitech'), ('micronics', 'micronics'))), ('etc', 'etc')], default='', max_length=20)),
                ('purchase_date', models.DateField(blank=True, default=datetime.date.today)),
                ('spec', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('equipment_id', models.IntegerField(primary_key=True, serialize=False)),
                ('seat', models.IntegerField(default=1)),
                ('name', models.CharField(default='No Name', max_length=10)),
                ('rank', models.CharField(choices=[('', '직급 선택'), ('s3', 's3'), ('s4', 's4'), ('s5', 's5'), ('s6', 's6'), ('s7', 's7'), ('s8', 's8'), ('freelancer', 'freelancer'), ('intern', 'intern'), ('contract', 'contract')], default='Not Ranked', max_length=20)),
                ('mainbody', models.CharField(blank=True, choices=[('', '노트북/데스크탑 선택'), ('노트북', (('그램', '그램'), ('울트라', '울트라'), ('삼성', '삼성'), ('아수스', '아수스'), ('한성', '한성'))), ('데스크톱', (('서버PC', '서버PC'), ('학습PC', '학습PC'), ('운영PC', '운영PC')))], max_length=20)),
                ('monitor', models.CharField(blank=True, choices=[('', '모니터 선택'), ('ViewSync', 'ViewSync'), ('LG', 'LG'), ('Samsung', 'Samsung')], max_length=20)),
                ('keyboard', models.CharField(blank=True, choices=[('', '키보드 선택'), ('Logitech(신형)', 'Logitech(신형)'), ('Logitech(구형)', 'Logitech(구형)'), ('기계식 키보드', '기계식 키보드')], max_length=20)),
                ('mouse', models.CharField(blank=True, choices=[('', '마우스 선택'), ('Logitech(신형)', 'Logitech(신형)'), ('Logitech(구형)', 'Logitech(구형)'), ('LG gram 마우스', 'LG gram 마우스'), ('삼성 노트북 마우스', '삼성 노트북 마우스'), ('Micronics', 'Micronics')], max_length=20)),
                ('smalldevice', models.CharField(blank=True, choices=[('', '소형 장비 선택'), ('외장HDD', '외장HDD'), ('외장SSD', '외장SSD'), ('NAS', 'NAS'), ('도킹스테이션', '도킹스테이션'), ('VPN 공유기', 'VPN 공유기'), ('허브', '허브')], max_length=20)),
                ('bigdevice', models.CharField(blank=True, choices=[('', '대형 장비 선택'), ('키오스크', '키오스크')], max_length=20)),
                ('accessory', models.CharField(blank=True, choices=[('', '액세서리 선택'), ('삼성 노트북 가방', '삼성 노트북 가방'), ('그램 노트북 가방', '그램 노트북 가방'), ('울트라 노트북 가방', '울트라 노트북 가방')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=20)),
                ('rank', models.CharField(choices=[('', '직급 선택'), ('s3', 's3'), ('s4', 's4'), ('s5', 's5'), ('s6', 's6'), ('s7', 's7'), ('s8', 's8'), ('freelancer', 'freelancer'), ('intern', 'intern'), ('contract', 'contract')], default='', max_length=20)),
                ('seat', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Usage',
            fields=[
                ('usage_id', models.IntegerField(primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('device_id', models.ForeignKey(db_column='device_id', on_delete=django.db.models.deletion.CASCADE, related_name='us_device', to='app_equipments.device')),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, related_name='user', to='app_equipments.user')),
            ],
        ),
        migrations.CreateModel(
            name='Amount',
            fields=[
                ('amount_id', models.IntegerField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField(default=1)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('device_id', models.ForeignKey(db_column='device_id', on_delete=django.db.models.deletion.CASCADE, related_name='am_device', to='app_equipments.device')),
            ],
        ),
    ]
