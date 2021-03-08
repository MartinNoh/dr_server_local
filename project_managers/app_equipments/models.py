from django.db import models

# Create your models here.
from django.db.models import DateField
import datetime


RANK_CHOICES = (
    ('', '직급 선택'),
    ('s3', 's3'),
    ('s4', 's4'),
    ('s5', 's5'),
    ('s6', 's6'),
    ('s7', 's7'),
    ('s8', 's8'),
    ('freelancer', 'freelancer'),
    ('intern', 'intern'),
    ('contract', 'contract'),
)


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, default='')  # CharField should be indicated with max_length
    rank = models.CharField(max_length=20, default='', choices=RANK_CHOICES)
    seat = models.IntegerField(default=1)

    def __str__(self):
        return str(self.name) + " | " + str(self.seat)


TYPE_CHOICES = (
    ('', '장비타입 선택'),
    ('notebook', 'notebook'),
    ('desktop', 'desktop'),
    ('monitor', 'monitor'),
    ('keyboard', 'keyboard'),
    ('mouse', 'mouse'),
    ('ex_storage', 'ex_storage'),
    ('network_eq', 'network_eq'),
    ('sound_eq', 'sound_eq'),
    ('accessory', 'accessory'),
    ('etc', 'etc'),
)

BRAND_CHOICES = (
    ('', '브랜드 선택'),
    ('notebook', (
        ('samsung_itech', 'samsung_itech'),
        ('gram512', 'gram512'),
        ('gram256', 'gram256'),
        ('ultra', 'ultra'),
        ('asus', 'asus'),
        ('hansung', 'hansung'),
    )),
    ('desktop', (
        ('deep_learning', 'deep_learning'),
        ('offer_interface', 'offer_interface'),
        ('run_client_app', 'run_client_app'),
    )),
    ('monitor', (
        ('samsung_itech', 'samsung_itech'),
        ('samsung', 'samsung'),
        ('lg', 'lg'),
        ('viewsync', 'viewsync'),
    )),
    ('keyboard/mouse', (
        ('samsung_itech', 'samsung_itech'),
        ('gram', 'gram'),
        ('ultra', 'ultra'),
        ('logitech', 'logitech'),
        ('micronics', 'micronics'),
    )),
    ('etc', 'etc'),
)


class Device(models.Model):
    device_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=20, default='', choices=TYPE_CHOICES)
    brand = models.CharField(max_length=20, default='', choices=BRAND_CHOICES)
    purchase_date = DateField(blank=True, default=datetime.date.today)
    spec = models.TextField(blank=True, default='')

    def __str__(self):
        return str(self.type) + " | " + str(self.brand)


class Amount(models.Model):
    amount_id = models.AutoField(primary_key=True)
    device_id = models.ForeignKey("Device", related_name="am_device", on_delete=models.CASCADE, db_column="device_id")
    amount = models.IntegerField(default=1)
    updated_at = models.DateTimeField(auto_now=True) # Update continuosly

    def __str__(self):
        return str(self.device_id) + " | " + str(self.amount)


class Usage(models.Model):
    usage_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey("User", related_name="user", on_delete=models.CASCADE, db_column="user_id")
    device_id = models.ForeignKey("Device", related_name="us_device", on_delete=models.CASCADE, db_column="device_id")
    updated_at = models.DateTimeField(auto_now=True) # Update continuosly

    def __str__(self):
        return str(self.user_id) + " | " + str(self.device_id)



class Equipment(models.Model):

    MAINBODY_CHOICES = (
        ('', '노트북/데스크탑 선택'),
        ('노트북', (
            ('그램', '그램'),
            ('울트라', '울트라'),
            ('삼성', '삼성'),
            ('아수스', '아수스'),
            ('한성', '한성'),
        )),
        ('데스크톱', (
            ('서버PC', '서버PC'),
            ('학습PC', '학습PC'),
            ('운영PC', '운영PC'),
        )),
    )

    MONITOR_CHOICES = (
        ('', '모니터 선택'),
        ('ViewSync', 'ViewSync'),
        ('LG', 'LG'),
        ('Samsung', 'Samsung'),
    )

    KEYBOARD_CHOICES = (
        ('', '키보드 선택'),
        ('Logitech(신형)', 'Logitech(신형)'),
        ('Logitech(구형)', 'Logitech(구형)'),
        ('기계식 키보드', '기계식 키보드'),
    )

    MOUSE_CHOICES = (
        ('', '마우스 선택'),
        ('Logitech(신형)', 'Logitech(신형)'),
        ('Logitech(구형)', 'Logitech(구형)'),
        ('LG gram 마우스', 'LG gram 마우스'),
        ('삼성 노트북 마우스', '삼성 노트북 마우스'),
        ('Micronics', 'Micronics'),
    )

    SMALLDEVICE_CHOICES = (
        ('', '소형 장비 선택'),
        ('외장HDD', '외장HDD'),
        ('외장SSD', '외장SSD'),
        ('NAS', 'NAS'),
        ('도킹스테이션', '도킹스테이션'),
        ('VPN 공유기', 'VPN 공유기'),
        ('허브', '허브'),
    )

    BIGDEVICE_CHOICES = (
        ('', '대형 장비 선택'),
        ('키오스크', '키오스크'),
    )

    ACCESSORY_CHOICES = (
        ('', '액세서리 선택'),
        ('삼성 노트북 가방', '삼성 노트북 가방'),
        ('그램 노트북 가방', '그램 노트북 가방'),
        ('울트라 노트북 가방', '울트라 노트북 가방'),
    )
    equipment_id = models.IntegerField(primary_key=True)
    seat = models.IntegerField(default=1)
    name = models.CharField(max_length=10, default='No Name') # CharField should be indicated with max_length
    rank = models.CharField(max_length=20, default='Not Ranked', choices=RANK_CHOICES)
    mainbody = models.CharField(max_length=20, blank=True, choices=MAINBODY_CHOICES)
    monitor = models.CharField(max_length=20, blank=True, choices=MONITOR_CHOICES)
    keyboard = models.CharField(max_length=20, blank=True, choices=KEYBOARD_CHOICES)
    mouse = models.CharField(max_length=20, blank=True, choices=MOUSE_CHOICES)
    smalldevice = models.CharField(max_length=20, blank=True, choices=SMALLDEVICE_CHOICES)
    bigdevice = models.CharField(max_length=20, blank=True, choices=BIGDEVICE_CHOICES)
    accessory = models.CharField(max_length=20, blank=True, choices=ACCESSORY_CHOICES)

    def __str__(self):
        return self.name