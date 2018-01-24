from django.db import models
from db.base_model import BaseModels

# Create your models here.


class PassPortManager(models.Manager):

    def add_one(self, username, password, email):
        obj = self.model(username=username, password=password, email=email)
        obj.save()
        return obj


class PassPort(BaseModels):
    username = models.CharField(max_length=20, verbose_name='用户名')
    password = models.CharField(max_length=40, verbose_name='密码')
    email = models.EmailField(verbose_name='邮箱地址')
    objects = PassPortManager()


    class Meta:
        db_table = 's_user_name'
