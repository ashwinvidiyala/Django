from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *

def index(request):
    if Course.objects.all():
    # for object in Course.objects.all():
    #     context = {
    #         'course_name': object.course_name,
    #         'description': object.description,
    #         'date_added': object.created_at,
    #     }
        context = {
            'course_data': Course.objects.all(),
        }
        return render(request, 'course/index.html', context)
    else:
        return render(request, 'course/index.html')

def create(request):
    course = Course.objects.create(course_name = request.POST['course_name'], description = request.POST['description'])
    return redirect('/course')


def destroy_confirmation(request, id):
    course = Course.objects.get(id = id)

    context = {
        'id': course.id,
        'course_name': course.course_name,
        'description': course.description,
    }

    return render(request, 'course/destroy_confirmation.html', context)

def destroy(request, id):

    if request.POST['submit'] == 'no':
        return redirect('/course')
    else:
        Course.objects.get(id=id).delete()
        return redirect('/course')
