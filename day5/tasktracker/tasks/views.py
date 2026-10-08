from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def task_list(request):
    if request.method == "GET":
        return JsonResponse({
            "message": "GET API successful"
        })

    if request.method == "POST":
        data = json.loads(request.body)
        return JsonResponse({
            "message": "POST API successful",
            "data": data
        })

    if request.method == "PUT":
        data = json.loads(request.body)
        return JsonResponse({
            "message": "PUT API successful",
            "data": data
        })

    if request.method == "DELETE":
        return JsonResponse({
            "message": "DELETE API successful"
        })

    return JsonResponse({
        "message": "Method not allowed"
    }, status=405)