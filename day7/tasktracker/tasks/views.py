from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Task
import json

@csrf_exempt
def task_api(request):
    if request.method == "GET":
        tasks = Task.objects.all()

        data = []

        for task in tasks:
            data.append({
                "id": task.id,
                "task_name": task.task_name,
                "description": task.description,
                "status": task.status,
                "created_date": task.created_date
            })

        return JsonResponse(data, safe=False)

    if request.method == "POST":
        data = json.loads(request.body)

        task = Task.objects.create(
            task_name=data.get("task_name"),
            description=data.get("description", ""),
            status=data.get("status", "pending")
        )

        return JsonResponse({
            "message": "Task created successfully",
            "id": task.id
        }, status=201)

    if request.method == "PUT":
        data = json.loads(request.body)
        task_id = data.get("id")

        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return JsonResponse({
                "message": "Task not found"
            }, status=404)

        task.task_name = data.get("task_name", task.task_name)
        task.description = data.get("description", task.description)
        task.status = data.get("status", task.status)
        task.save()

        return JsonResponse({
            "message": "Task updated successfully"
        })

    if request.method == "DELETE":
        data = json.loads(request.body)
        task_id = data.get("id")

        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return JsonResponse({
                "message": "Task not found"
            }, status=404)

        task.delete()

        return JsonResponse({
            "message": "Task deleted successfully"
        })

    return JsonResponse({
        "message": "Method not allowed"
    }, status=405)