# Generated by Django 3.0.3 on 2020-03-03 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banner',
            old_name='file',
            new_name='img_url',
        ),
        migrations.AlterField(
            model_name='banner',
            name='id',
            field=models.UUIDField(default='463f527a5d1611ea86f4acd1b8d2566c', editable=False, primary_key=True, serialize=False, verbose_name='主键ID'),
        ),
    ]