from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem
# Create your views here.


def todoView(request):
    all_todo = TodoItem.objects.all()
    return render(request, 'todo.html', {'all_items': all_todo})


def addTodo(request):
    new_item = TodoItem(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')


def deleteTodo(request, todo_id):
    item_delete = TodoItem.objects.get(id=todo_id)
    item_delete.delete()
    return HttpResponseRedirect('/todo/')
