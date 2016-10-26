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
    serial_number = models.IntegerField(default=0, max_length=30)
    class_level = models.IntegerField(default=0)
    priority_level = models.IntegerField(default=0)
    status_level = models.IntegerField(default=0)
    stage_level = models.IntegerField(default=0)
    product_version = models.CharField(max_length=30)
    product_type = models.CharField(max_length=30)
    change_date = models.DateTimeField('change date')

    def __str__(self):
        return self.project_text