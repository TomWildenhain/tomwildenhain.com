from django.db import models
import os

# Create your models here.
short_max_len = 200


class Project(models.Model):
    project_title = models.CharField(max_length=short_max_len)
    sidebar_title = models.CharField(max_length=short_max_len, blank=True, default="")
    div_id = models.CharField(max_length=short_max_len)
    start_date = models.CharField(max_length=short_max_len, blank=True, default="")
    end_date = models.CharField(max_length=short_max_len, blank=True, default="")
    project_description = models.TextField()
    github_link = models.CharField(max_length=short_max_len, blank=True, default="")
    index = models.PositiveIntegerField(default=0)
    ordering = ('index',)
    def __str__(self):
        return self.project_title


class SkillToken(models.Model):
    project = models.ForeignKey(Project, models.CASCADE)
    skill_name = models.CharField(max_length=short_max_len)
    index = models.PositiveIntegerField(default=0)
    ordering = ('index',)
    def __str__(self):
        return self.skill_name

def get_image_path(instance, filename):
    _, extension = os.path.splitext(filename)
    return 'projects/' + instance.project.div_id + '/' + 'img' + str(instance.index) + extension

class Image(models.Model):
    project = models.ForeignKey(Project, models.CASCADE)
    image = models.ImageField(upload_to=get_image_path)
    caption = models.CharField(max_length=short_max_len, blank=True, default="")
    hide_on_small_screens = models.BooleanField(default=False)
    index = models.PositiveIntegerField(default=0)
    ordering = ('index',)
    def __str__(self):
        return str(self.project) + " image " + str(self.index)