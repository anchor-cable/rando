from django.shortcuts import render,redirect
from .models import TodoList, Category
from random import randint
def index(request): #the index view
    chosenCategory = Category.objects.get(name='5分')
    todos = TodoList.objects.filter(category=chosenCategory)
    last = todos.count() -1
    index = randint(0,last)
    todo = todos[index] #quering all todos with the object manager
    categories = Category.objects.all() #getting all categories with object manager
    if request.method == "POST": #checking if the request method is a POST
        if "taskAdd" in request.POST: #checking if there is a request to add a todo
            title = request.POST["description"] #title
            date = str(request.POST["date"]) #date
            category = request.POST["category_select"] #category
            content = title + " -- " + date + " " + category #content
            Todo = TodoList(title=title, content=content, category=Category.objects.get(name=category))
            Todo.save() #saving the todo
            return redirect("/") #reloading the page
        if "taskDelete" in request.POST: #checking if there is a request to delete a todo
            checkedlist = request.POST["checkedbox"] #checked todos to be deleted
            for todo_id in checkedlist:
                todo = TodoList.objects.get(id=int(todo_id)) #getting todo id
                todo.delete() #deleting todo
    return render(request, "index.html", {"todo": todo, "categories":categories})
# Create your views here.
