# Generated by Django 4.0.5 on 2022-11-28 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_exchange'),
    ]

    operations = [
        migrations.AddField(
            model_name='exchange',
            name='Details',
            field=models.CharField(default=1, max_length=100, verbose_name='卡片详情'),
            preserve_default=False,
        ),
    ]
