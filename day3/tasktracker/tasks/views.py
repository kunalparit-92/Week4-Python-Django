from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def get_tasks(request):
    if request.method == "GET":
        return JsonResponse({
            "message": "GET request successful"
        })

    if request.method == "POST":
        data = json.loads(request.body)
        return JsonResponse({
            "message": "POST request successful",
            "data": data
        })

    if request.method == "PUT":
        data = json.loads(request.body)
        return JsonResponse({
            "message": "PUT request successful",
            "data": data
        })

    if request.method == "DELETE":
        return JsonResponse({
            "message": "DELETE request successful"
        })

    return JsonResponse({
        "message": "Method not allowed"
    }, status=405)