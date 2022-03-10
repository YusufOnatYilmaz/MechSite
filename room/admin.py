from django.contrib import admin
from .models import User, Project, Room, Item

admin.site.register(User)
admin.site.register(Project)
admin.site.register(Room)
admin.site.register(Item)
