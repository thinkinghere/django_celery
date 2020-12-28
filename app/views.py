# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.shortcuts import render
from django.http.response import JsonResponse
from app.tasks import Upload, add


# Create your views here.

def doTask(request):
    print('start task!')
    Upload.delay()  # 异步任务，这里不会卡住，尽管有延时
    print('end task!')
    return JsonResponse({"type": 'success'})


def test(request):
    res = add.delay(1, 2)
    res = add.AsyncResult(res.task_id).get()
    return JsonResponse({'success': res})
