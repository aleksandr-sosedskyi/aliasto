from django.db import models
from django.utils import timezone


class User(models.Model):
    telegram_id = models.IntegerField(null=True)
    username = models.CharField(max_length=50, null=True, blank=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    views = models.IntegerField(null=True, blank=True, default=0)
    created_at = models.DateTimeField(default=timezone.now())

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f'{self.username or ""} - {self.views}'


class Item(models.Model):
    code = models.CharField(max_length=50)
    link = models.CharField(max_length=100)
    views = models.IntegerField(null=True, blank=True, default=0)
    created_at = models.DateTimeField(default=timezone.now())

    class Meta:
        db_table = 'items'
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self):
        return f'{self.code} - {self.views}'
