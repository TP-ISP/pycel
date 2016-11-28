import datetime

from django.db import models
from django.utils import timezone

# class Question(models.Model):
#
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
#     def __str__(self):
#         return self.question_text
#
#     def was_published_recently(self):
#         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.choice_text

class Project(models.Model):
    LEADER = (
        ('W', 'WenZhenYu'),
        ('Z', 'ZhongLianBo'),
    )
    PRODUCT_TYPE = (
        ('A', 'ADSL'),
        ('B', 'BB'),
    )
    STATUS_LEVEL = (
        ('N', 'Normal'),
        ('U', 'ABNORMAL'),
    )
    PRODUCT_MANAGER = (
        ('C', 'Conner'),
        ('G', 'Garvin'),
        ('H', 'Harvey'),
        ('W', 'Will'),
    )
    serial_number = models.IntegerField(default=0)
    class_level = models.IntegerField(default=0)
    priority_level = models.IntegerField(default=0)
    status_level = models.CharField(max_length=1, choices=STATUS_LEVEL, default='N')
    stage_level = models.IntegerField(default=0)
    product_version = models.CharField(max_length=30, default="1.0.0")
    product_type = models.CharField(max_length=1, choices=PRODUCT_TYPE, default='A')
    leader_name = models.CharField(max_length=1, choices=LEADER, default='W')
    change_date = models.DateTimeField('change date')
    area_name = models.CharField(max_length=30, default="")
    guest_name = models.CharField(max_length=30, default="")
    rd_name = models.CharField(max_length=30, default="")
    pm_name = models.CharField(max_length=1, choices=PRODUCT_MANAGER, default='C')

    def __str__(self):
        return self.product_version

    def was_published_recently(self):
         return self.change_date >= timezone.now() - datetime.timedelta(days=1)