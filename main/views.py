
from django.shortcuts import render
from .models import About, CourseCategory, Course, Staff


def index(request):
    about_data = About.objects.all()[:1]
    course_categories = CourseCategory.objects.all()[:4]
    courses = Course.objects.all()[:3]
    staffs = Staff.objects.all()[:4]
    about = None
    if len(about_data) > 0:
        about = about_data[0]
    context = {
        'about': about,
        'course_categories': course_categories,
        'courses': courses,
        'staffs': staffs,
    }
    return render(request, 'index.html', context)

def about(request):
    about_data = About.objects.all()[:1]
    staffs = Staff.objects.all()[:4]
    about = None
    if len(about_data) > 0:
        about = about_data[0]
    context = {
        'about': about,
        'staffs': staffs,
    }
    return render(request, 'about.html', context)

def courses(request):
    course_categories = CourseCategory.objects.all()[:4]
    courses = Course.objects.all()
    context = {
        "courses": courses,
        "course_categories": course_categories,
    }
    return render(request, 'courses.html', context)

def contact(request):
    return render(request, 'contact.html')

def gallery(request):
    return render(request, 'gallery.html')

def staff(request):
    return render(request, 'staff.html')

def event(request):
    return render(request, 'event.html')

