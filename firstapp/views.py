from django.shortcuts import render
from .models import Course
from .serializers import CourseSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.

# Show all courses
def course_index(request):
    courses = Course.objects.all() # complex data
    serializer = CourseSerializer(courses, many = True) # serialize the complex data (many objects)
    json_data = JSONRenderer().render(serializer.data) # convert into JSON
    
    return HttpResponse(json_data, content_type='application/json') # return http response

# Create specific course
def course_show(request, id):
    course = Course.objects.get(id = id) # complex data
    serializer = CourseSerializer(course) # serialize the complex data (many objects)
    json_data = JSONRenderer().render(serializer.data) # convert into JSON
    
    return HttpResponse(json_data, content_type='application/json') # return http response