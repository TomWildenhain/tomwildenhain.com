from django.db import models

# Create your models here.
short_max_len = 200

class Education(models.Model):
    class Meta:
        verbose_name_plural = "education"
    institution_name = models.CharField(max_length=short_max_len)
    location = models.CharField(max_length=short_max_len)
    degree_title = models.CharField(max_length=short_max_len, blank=True, default='')
    index = models.PositiveIntegerField(default=0)
    ordering = ['index']
    def __str__(self):
        return self.institution_name

class Honor(models.Model):
    education = models.ForeignKey(Education, models.CASCADE)
    honor_name = models.CharField(max_length=short_max_len)
    index = models.PositiveIntegerField(default=0)
    ordering = ['index']
    def __str__(self):
        return self.honor_name

class Experience(models.Model):
    position_title = models.CharField(max_length=short_max_len)
    organization_name = models.CharField(max_length=short_max_len)
    start_date = models.CharField(max_length=short_max_len, blank=True, default="")
    end_date = models.CharField(max_length=short_max_len, blank=True, default="")
    index = models.PositiveIntegerField(default=0)
    ordering = ['index']
    def __str__(self):
        return self.position_title


class ExperienceDescription(models.Model):
    experience = models.ForeignKey(Experience, models.CASCADE)
    description = models.TextField()
    index = models.PositiveIntegerField(default=0)
    ordering = ['index']
    def __str__(self):
        return self.description


class Project(models.Model):
    project_title = models.CharField(max_length=short_max_len)
    collaborators = models.CharField(max_length=short_max_len, blank=True, default="")
    start_date = models.CharField(max_length=short_max_len, blank=True, default="")
    end_date = models.CharField(max_length=short_max_len, blank=True, default="")
    index = models.PositiveIntegerField(default=0)
    ordering = ['index']
    def __str__(self):
        return self.project_title


class ProjectDescription(models.Model):
    project = models.ForeignKey(Project, models.CASCADE)
    description = models.TextField()
    index = models.PositiveIntegerField(default=0)
    ordering = ['index']
    def __str__(self):
        return self.description


class Skill(models.Model):
    skill_title = models.CharField(max_length=short_max_len)
    confidence = models.IntegerField()
    ordering = ('-confidence',)
    def __str__(self):
        return self.skill_title


