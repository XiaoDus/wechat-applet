# Generated by Django 4.0.5 on 2022-12-01 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_exchange_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='exchange',
            name='imgUrl',
            field=models.CharField(default=1, max_length=200, verbose_name='图片'),
            preserve_default=False,
        ),
    ]
