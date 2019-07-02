from django.contrib import admin


from . import models


class ToDoListAdmin(admin.ModelAdmin):
    list_display = ("task", "due_date")


admin.site.register(models.ToDoList, ToDoListAdmin)

