import datetime

from django.db import models
from django.utils import timezone

class Project(models.Model):
    PRODUCT_TYPE = (
        ('A', 'ADSL'),
        ('B', 'BB'),
    )
    STATUS_LEVEL = (
        ('N', 'Normal'),
        ('U', 'ABNORMAL'),
    )
    serial_number = models.IntegerField(default=0)
    class_level = models.IntegerField(default=1)
    priority_level = models.IntegerField(default=0)
    status_level = models.CharField(max_length=1, choices=STATUS_LEVEL, default='N')
    stage_level = models.IntegerField(default=0)
    product_version = models.CharField(max_length=30, default="Default Version")
    product_type = models.CharField(max_length=1, choices=PRODUCT_TYPE, default='A')
    leader_name = models.CharField(max_length=20, default='Default Leader')
    change_date = models.DateTimeField('change date')
    area_name = models.CharField(max_length=30, default="Default Area")
    guest_name = models.CharField(max_length=30, default="Default Guest")
    rd_name = models.CharField(max_length=30, default="Default Research Engineer")
    pm_name = models.CharField(max_length=30, default='Conner')
    isp = models.CharField(max_length=30, default='Default ISP')
    is_visible = models.IntegerField(default=0)

    def __str__(self):
        return "%s, %s, %s" % (self.product_version, self.pm_name, self.rd_name)
