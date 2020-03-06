from django.db import models

# Create your models here.

import uuid

from datetime import datetime


class db_classify(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, verbose_name='主键ID')

    title = models.CharField(max_length=10, verbose_name='分类名称')

    index = index = models.PositiveSmallIntegerField(default=0, verbose_name="顺序")

    create_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    class Meta:
        db_table = 'db_classify'

        verbose_name = '分类'
