from django.db import models
from datetime import datetime
import uuid
class Banner(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,verbose_name='主键ID')

    title = models.CharField(max_length=255, null=True, verbose_name="轮播图标题")

    desc = models.CharField(max_length=255, null=True, verbose_name="轮播图描述")

    img_url = models.FileField(verbose_name='图片')

    create_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")

    index = models.PositiveSmallIntegerField(default=0, verbose_name="顺序")

    external_url = models.CharField(max_length=255, null=True, verbose_name='外链地址URL')

    class Meta:
        db_table = 'db_banner'

        verbose_name = '轮播图'
