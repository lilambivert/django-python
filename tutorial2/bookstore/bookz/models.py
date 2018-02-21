from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Book(models.Model):
    book = models.CharField(max_length=250)
    price = models.IntegerField()

    def __str__(self):
        return self.book

class Purchase(models.Model):
    user = models.ForeignKey(User, related_name='user_info')
    price = models.IntegerField()
    address = models.CharField(max_length=250)
    book = models.CharField(max_length=250)

    def __str__(self):
        return self.address
