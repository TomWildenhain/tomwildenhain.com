from django.contrib import admin
from projects.models import *


class SkillTokenAdmin(admin.StackedInline):
    model = SkillToken
    extra = 1
    ordering = ('index',)

class ImageAdmin(admin.StackedInline):
    model = Image
    extra = 1
    ordering = ('index',)

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ImageAdmin, SkillTokenAdmin]
    ordering = ('index',)

admin.site.register(Project, ProjectAdmin)