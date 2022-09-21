from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class TaskView(View):
    def get(self, request):
        return render(request, 'task/tasks.html', {
            'name': 'RED'
        })
