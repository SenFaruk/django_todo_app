from django.shortcuts import render,redirect,get_object_or_404
from .models import Todo
from .forms import TodoAddForm, TodoUpdateForm

# Create your views here.
def home(request):
    return render(request, "to_do_app/home.html")

def todo_list(request):
    todos = Todo.objects.all() # orm komutu
    form = TodoAddForm()
    if request.method == 'POST':
        print(request.POST)
        form = TodoAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")
    context = {
        'todos': todos,
        'form': form,
    }
    return render(request, "to_do_app/todo_list.html", context)

def todo_add(request): 
    form = TodoAddForm()
    if request.method == 'POST':
        print(request.POST)
        form = TodoAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list") # urls.py daki path in name
    
    context = {
        'form': form,
    }
    
    return render(request, "to_do_app/todo_add.html", context)

def todo_update(request, id):
    # todo = Todo.objects.get(id=id)
    todo = get_object_or_404(Todo, id=id)
    form = TodoUpdateForm(instance=todo)
    if request.method == 'POST':
        form = TodoUpdateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("list") 
    context = {
        'form':form,
        'todo': todo,        
    }
    return render(request, "to_do_app/todo_update.html", context)

def todo_delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == 'POST':
        todo.delete()
        return redirect("list") # urls.py 
    context = {
        'todo' : todo,
    }
    
    return render(request, "to_do_app/todo_delete.html", context)
        
