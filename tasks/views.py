from django.shortcuts import render, redirect
from .models import TodoDatabase
from django.contrib import messages

def indexHome(request):

        if request.method == 'POST':
                taskName = request.POST['task']

                if len(taskName) < 5:
                        messages.warning(request, "Task Must Contain more Than 5 Character!!!")
                        return redirect('Homepage')

                todo = TodoDatabase(task_name = taskName, slug=taskName)
                todo.save()
                messages.success(request, "Your Task Has Been Added To Our Database!")
                redirect('Homepage')

        todo = TodoDatabase.objects.all()[::-1]

        context = {'todoData': todo, 'title':'TODO APP'}
        return render(request, 'tasks/index.html', context)

def deleteTask(request, slug):
        todo = TodoDatabase.objects.get(slug=slug)
        todo.delete()
        messages.success(request, "Task has Been Deleted Successfully!!!")
        return redirect("Homepage")

def editTask(request, slug):
        todo = TodoDatabase.objects.get(slug=slug)

        if request.method == "POST":
                updatedTask = request.POST['updateTask']+' + '

                todoUpdate = TodoDatabase.objects.get(slug=slug)
                todoUpdate.task_name = updatedTask
                todoUpdate.slug = slug
                todoUpdate.save()
                messages.success(request, "Task Has Been Successfully Updated!")
                return redirect('Homepage')

        params = {'task':todo, 'title':todo.slug}

        return render(request, 'tasks/editTask.html', params)