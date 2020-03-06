# Generated by Django 3.0.3 on 2020-03-03 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0002_auto_20200303_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='desc',
            field=models.CharField(max_length=255, null=True, verbose_name='轮播图描述'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='id',
            field=models.UUIDField(default='63e2450c5d1611ea8145acd1b8d2566c', editable=False, primary_key=True, serialize=False, verbose_name='主键ID'),
        ),
    ]