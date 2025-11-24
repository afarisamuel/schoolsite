
from django.shortcuts import render
from .models import About, CourseCategory, Course, Staff


def index(request):
    about = About.objects.all()[:1]
    course_categories = CourseCategory.objects.all()[:4]
    courses = Course.objects.all()
    staffs = Staff.objects.all()[:4]
    context = {
        'about': about,
        'course_categories': course_categories,
        'courses': courses,
        'staffs': staffs,
    }
    return render(request, 'index.html', context)

def about(request):
    about = About.objects.all()[:1]
    context = {
        'about': about
    }
    return render(request, 'about.html', context)

def courses(request):
    return render(request, 'courses.html')

def contact(request):
    return render(request, 'contact.html')

def gallery(request):
    return render(request, 'gallery.html')

def staff(request):
    return render(request, 'staff.html')

def event(request):
    return render(request, 'event.html')

