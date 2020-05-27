from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Todo
from .forms import TodoForm,NewTodoForm


def index(request):
    todo_list = Todo.objects.order_by('id')
    # form = TodoForm()
    newtodoform = NewTodoForm()

    context = {'todo_list': todo_list, 'form': newtodoform}
    return render(request, 'todo/index.html', context)


@require_POST
def addtodo(request):
    # form = TodoForm(request.POST)
    todo_10 = Todo.objects.get(pk=10)
    newtodoform = NewTodoForm(request.POST, instance=todo_10)
    if newtodoform.is_valid():
        # new_todo = Todo(activity=form.cleaned_data['activity'])
        # new_todo.save()
        new_todo = newtodoform.save()

    return redirect('index')


def completetodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()
    return redirect('index')


def deletecompleted(request):
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('index')


def deleteall(request):
    Todo.objects.all().delete()

    return redirect('index')