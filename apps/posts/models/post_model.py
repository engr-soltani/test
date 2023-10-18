from django.db import models

class Post(models.Model):

    user = models.ForeignKey('accounts.User',on_delete=models.CASCADE)
    title = models.CharField('Title',max_length=120)
    description = models.CharField('Description',max_length=256)
    number_rates = models.IntegerField(default=0)
    avg_rates = models.IntegerField(default=0)
    created_time = models.DateTimeField('created time', auto_now_add=True)
    updated_time = models.DateTimeField('updated time', auto_now=True)
