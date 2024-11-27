from django.shortcuts import render , redirect
from .models import Task
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.db import transaction

def task(request):
    if request.method == 'POST':
        taskname=request.POST.get('taskname')
        startingdate=request.POST.get('startingdate')
        endingdate=request.POST.get('endingdate')
        status=request.POST.get('status')

        Task.objects.create(
            Taskname=taskname,
            Startingdate=startingdate,
            Endingdate=endingdate,
            Status=status
        )
        if request.POST.get('submit') == 'save':
            messages.success(request, 'Task data has been saved. You can add more Tasks.')
            return render(request, 'tasks/tasks.html')  # Stay on the same form page

        # If "Submit" button was clicked
        if request.POST.get('submit') == 'submit':
            messages.success(request, 'Task data has been successfully submitted.')
            return redirect('task_list')  # Redirect to the employee list page

    return render(request, 'tasks/tasks.html')

def task_list(request):
    tasks = Task.objects.all()  # Query to get all task records
    return render(request, 'tasks/tasks-list.html', {'tasks': tasks})

def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    messages.success(request, 'Task deleted successfully.')

    # Renumber the serial_number field for all remaining tasks
    with transaction.atomic():
        tasks = Task.objects.all().order_by('id')
        for index, task in enumerate(tasks, start=1):
            task.serial_number = index
            task.save(update_fields=['serial_number'])

    return redirect('task_list')

def update_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        task.Taskname = request.POST.get('taskname')  # Match the name attribute in the form
        task.Startingdate = request.POST.get('startingdate')  # Match the name attribute in the form
        task.Endingdate = request.POST.get('endingdate')  # Match the name attribute in the form
        task.Status = request.POST.get('status')  # Match the name attribute in the form
        task.save()
        messages.success(request, 'task data updated.')
        return redirect('task_list')  # Replace with the URL name for your task list

    return render(request, 'tasks/update-tasks.html', {'task': task})