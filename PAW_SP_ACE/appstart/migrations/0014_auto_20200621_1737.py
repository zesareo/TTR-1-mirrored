# Generated by Django 3.0.5 on 2020-06-21 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appstart', '0013_auto_20200616_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='tramite',
            name='firma',
            field=models.CharField(default='', max_length=128, verbose_name='firma'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tramite',
            name='qr',
            field=models.CharField(default='', max_length=128, verbose_name='qr'),
            preserve_default=False,
        ),
    ]
