from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

from api import models
from api.models import Task, TaskList

def get_task_lists(request):
    task_lists = models.TaskList.objects.all()
    json_task_list =[t.to_json() for t in task_lists]
    return JsonResponse(json_task_list, safe=False)

def get_tasks(request, pk):
    try:
        task_list = TaskList.objects.get(pk=id)
    except TaskList.DoesNotExist as e:
        return JsonResponse({"error": str(e)}, safe=False)
    tasks = task_list.task_set.all()
    json_tasks = [t.to_json() for t in tasks]
    return JsonResponse(json_tasks, safe=False)