from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator  # 限制IntegerField的取值范围


class xiaoduIntegral(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=6)
    Integral = models.IntegerField(verbose_name='小肚的积分', validators=[MinValueValidator(0)], default=0)


class xiaoxuanIntegral(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=6)
    Integral = models.IntegerField(verbose_name='小轩的积分', validators=[MinValueValidator(0)], default=0)


class Task(models.Model):
    id = models.AutoField(verbose_name='ID', primary_key=True)
    taskName = models.CharField(verbose_name='任务名称', max_length=10)
    taskDetails = models.CharField(verbose_name='任务详情', max_length=100)
    taskAward = models.CharField(verbose_name='任务奖励积分', max_length=2)
    setTime = models.CharField(verbose_name='添加时间', max_length=20)
    isFinishChoice = (
        (1, '完成'),
        (2, '待完成')
    )
    isFinish = models.SmallIntegerField(choices=isFinishChoice, default=2)


class Exchange(models.Model):
    '''商品卡'''
    name = models.CharField(verbose_name='商品名称', max_length=10)
    Details=models.CharField(verbose_name='卡片详情', max_length=100)
    numCommodity = models.IntegerField(verbose_name='商品卡数量', validators=[MinValueValidator(0)], default=0)
    imgUrl=models.CharField(verbose_name='图片',max_length=200)
# Create your models here.
