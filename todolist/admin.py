from django.contrib import admin
from . import models
class TodoListAdmin(admin.ModelAdmin):
    list_display = ("title",  "created")
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
admin.site.register(models.TodoList, TodoListAdmin)
admin.site.register(models.Category, CategoryAdmin)
# Register your models here.
