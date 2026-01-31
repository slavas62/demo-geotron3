from django.contrib import admin

from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'visible', 'description', 'image', 'url', 'position',)
    ordering = ('position',)

admin.site.register(Project, ProjectAdmin)
