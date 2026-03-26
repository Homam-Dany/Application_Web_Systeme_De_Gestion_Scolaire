from django.shortcuts import render
from django.http import HttpResponse

def student_list(request):
    return HttpResponse('Student List Placeholder')

def add_student(request):
    return HttpResponse('Add Student Placeholder')
