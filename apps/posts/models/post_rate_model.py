from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class PostRate(models.Model):
    post = models.ForeignKey('Post',on_delete=models.CASCADE, related_name='postRate')
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    rate = models.IntegerField(default=0,validators=[MaxValueValidator(5),MinValueValidator(0)])
    created_time = models.DateTimeField('created time', auto_now_add=True)