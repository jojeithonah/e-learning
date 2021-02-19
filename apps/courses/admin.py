from django.contrib import admin

# Register your models here.
from django.utils.translation import ugettext as _
from . import models 



@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'previous_course',)

class QuestionInline(admin.TabularInline):
    model = models.Question


@admin.register(models.Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [
        QuestionInline,
    ]

@admin.register(models.QuestionUser)
class QuestionUserAdmin(admin.ModelAdmin):
    list_display = ('user',)