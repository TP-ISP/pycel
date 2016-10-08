from django.db import models


class Clauses(models.Model):
    clause = models.IntegerField(default=2)
    clause_title = models.CharField(max_length=100)

class Item(models.Model):
    author = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    department = models.IntegerField(max_length=10)
    content = models.TextField()
