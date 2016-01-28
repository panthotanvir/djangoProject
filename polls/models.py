from django.db import models
from django.utils import timezone

import datetime

# Create your models here.

class SignUp(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length =150, null = True)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
    update = models.DateTimeField(auto_now_add = False, auto_now = True)

    def __unicode__(self):
        return  self.email


class Document(models.Model):
    docfile = models.FileField(upload_to='documents/')














# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
#     def __str__(self):
#     	return self.question_text
#
#     def was_published_recently(self):
#         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
#     was_published_recently.admin_order_field = 'pub_date'
#     was_published_recently.boolean = True
#     was_published_recently.short_description = 'Published recently?'
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.choice_text