import datetime
from django.core import serializers #将数据库 Queryset 格式的数据序列化成 json
# from django.forms.models import model_to_dict #将数据库 Queryset 格式的数据转换成 dict

from django.http import JsonResponse
import json
from app import models
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def Integral(request):
    '''积分'''
    xuanQuerySet = models.xiaoxuanIntegral.objects.all()
    # models.Task.objects.all().delete()

    for i in xuanQuerySet:
        xuanName = i.name
        xuanIntegral = i.Integral

    result = {
        "stutic": True,
        "data": {
           
            'xiaogao': {
                'name': xuanName,
                'Integral': xuanIntegral
            }
        }
    }
    if request.method == 'POST':
        # return JsonResponse(result)
        return JsonResponse({'status': result})
    elif request.method=='GET':
        integral=request.GET.get('integral')
        print(integral)
        # 获取小轩的积分
        xxAward = models.xiaoxuanIntegral.objects.values('Integral')[0]['Integral']
        endIntegral = int(xxAward) - int(integral)
        # 修改积分
        models.xiaoxuanIntegral.objects.filter(id=1).update(Integral=endIntegral)
        print(xxAward)

        return JsonResponse({'status': result})


@csrf_exempt
def task(request):
    '''获取任务'''
    if request.method == 'POST':

        taskList=serializers.serialize('json',models.Task.objects.all().order_by('-setTime'))
        taskStr = json.loads(taskList) #把 json 数据转换为字典
        result = {
            "code": 200,
            "taskList":taskStr
        }
    return JsonResponse({'status': result})



@csrf_exempt
def taskFinish(request):
    '''任务详情'''
    if request.method=='GET':
        # 获取任务ID
        nid=request.GET.get('id')
        task_finish=serializers.serialize('json',models.Task.objects.filter(id=nid))
        taskStr = json.loads(task_finish)  # 把 json 数据转换为字典
        result = {
            "code": 200,
            "taskList": taskStr
        }
        return JsonResponse({'status': result})
    elif request.method=='POST':
        data = request.body.decode("utf-8")  # 把接收的数据解码为 utf-8
        json_data = json.loads(data)  # 把 json 数据转换为字典
        print(json_data)
        # 获取任务ID和奖励积分
        nid=json_data['Task']['id']
        taskAward=json_data['Task']['taskAward']
        # 获取小轩的积分
        xxAward=models.xiaoxuanIntegral.objects.values('Integral')[0]['Integral']
        print(xxAward)
        if 'taskName' in json_data['Task'] and 'taskDetails' in json_data['Task'] and 'taskAward' in json_data['Task']:
            '''判断是否是修改数据否则是完成任务'''
            TaskName = json_data['Task']['taskName']
            TaskDetails = json_data['Task']['taskDetails']
            TaskAward = json_data['Task']['taskAward']
            print(TaskName,TaskDetails,TaskAward,nid)
            models.Task.objects.filter(id=nid).update(taskName=TaskName, taskDetails=TaskDetails, taskAward=TaskAward)
            return JsonResponse({'code': 200})

        # 完成任务
        models.Task.objects.filter(id=nid).update(isFinish=1)
        # 更新小轩的积分
        endAward=int(taskAward)+int(xxAward)
        models.xiaoxuanIntegral.objects.filter(name='小轩').update(Integral=endAward)
        return JsonResponse({'code': 200})

@csrf_exempt
def exchange(request):
    '''兑换'''
    if request.method == 'POST':
        '''前端发送的数据在body里'''
        data = request.body.decode("utf-8")  # 把接收的数据解码为 utf-8
        json_data = json.loads(data)  # 把 json 数据转换为字典

        # 获取兑换商品积分和商品名字
        integral_send=json_data['integral']
        commodity_send=json_data['name']
        print(commodity_send)
        # 获取小轩积分和任务卡数量
        integral=models.xiaoxuanIntegral.objects.all().values('Integral')[0]['Integral']

        num=models.Exchange.objects.filter(name=commodity_send).values()[0]['numCommodity'] +1
        endIntegral=int(integral)-int(integral_send)
        # 修改积分
        models.xiaoxuanIntegral.objects.filter(id=1).update(Integral=endIntegral)
        # 修改商品卡数量
        models.Exchange.objects.filter(name=commodity_send).update(numCommodity=num)

        result = {
            "stutic": 200
        }
        return JsonResponse({'status': result})

@csrf_exempt
def sollList(request):
    '''卡片List'''
    if request.method=='POST':
        '''兑换卡片'''
        solList = serializers.serialize('json', models.Exchange.objects.all())
        solkDict = json.loads(solList)  # 把 json 数据转换为字典
        result = {
            "stutic": 200,
            'data':solkDict
        }
        return JsonResponse({'status': result})
    elif request.method=="GET":
        '''使用卡片'''
        getName=request.GET.get('name')
        num=models.Exchange.objects.filter(name=getName).values()[0]['numCommodity'] -1
        if num<=0:
            models.Exchange.objects.filter(name=getName).update(numCommodity=0)
        # 修改商品卡数量
        models.Exchange.objects.filter(name=getName).update(numCommodity=num)
        result = {
            "stutic": 200,
        }
        return JsonResponse({'status': result})


@csrf_exempt
def addTask(request):
    '''添加任务'''
    if request.method=='POST':
        '''前端发送的数据在body里'''
        result = {
            "stutic": 200
        }
        data=request.body.decode("utf-8")  #把接收的数据解码为 utf-8
        json_data=json.loads(data)  #把 json 数据转换为字典

        TaskName=json_data['Task']['TaskName']
        TaskDetails=json_data['Task']['TaskDetails']
        TaskAward=json_data['Task']['TaskAward']
        setTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        models.Task.objects.create(taskName=TaskName,taskDetails=TaskDetails,taskAward=TaskAward,setTime=setTime)
        return JsonResponse({'status': result})


# 删除任务
def taskDelete(request):
    '''删除任务'''
    if request.method=='GET':
        nid=request.GET.get('nid')
        models.Task.objects.filter(id=nid).delete()
    return JsonResponse({'status': 200})
# Create your views here.
