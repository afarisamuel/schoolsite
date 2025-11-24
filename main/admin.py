from django.contrib import admin
from .models import About, CourseCategory, Course, Event, Staff
# Register your models here.

admin.site.register(About)
admin.site.register(CourseCategory)
admin.site.register(Course)
admin.site.register(Event)
admin.site.register(Staff)