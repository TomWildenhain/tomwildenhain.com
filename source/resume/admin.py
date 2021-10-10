from django.contrib import admin
from resume.models import *
from orderable_inlines import OrderableTabularInline

# Register your models here.

def register_inline(ParentModel, InlineModel):
    class InlineAdmin(admin.StackedInline):
        model = InlineModel
        extra = 1
        ordering = ('index',)
    class ParentAdmin(admin.ModelAdmin):
        inlines = [InlineAdmin]
        ordering = ('index',)
    admin.site.register(ParentModel, ParentAdmin)

register_inline(Education, Honor)
register_inline(Experience, ExperienceDescription)
register_inline(Project, ProjectDescription)

class SkillAdmin(admin.ModelAdmin):
    ordering = ('-confidence',)

admin.site.register(Skill, SkillAdmin)