from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

from .models import Task

# Create your views here.

class TaskView(View):
    def get(self, request):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':    
            tasks = list(Task.objects.values())
            return JsonResponse(tasks, safe=False, status=200)
        return render(request, 'task/tasks.html', {
            'name': 'RED'
        })
