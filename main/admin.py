from django.contrib import admin
from django.db import models
from tinymce.widgets import TinyMCE
from .models import About, CourseCategory, Course, Event, Staff, Gallery
# Register your models here.

admin.site.register(About)
admin.site.register(CourseCategory)
admin.site.register(Course)
admin.site.register(Staff)
admin.site.register(Gallery)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }
    list_display=["author","title", "subtitle", ]