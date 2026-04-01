import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school.settings')
django.setup()

from faculty.models import Subject
from student.models import Student

print("Unique Subject Class Names:")
for cn in Subject.objects.values_list('class_name', flat=True).distinct():
    print(f"- {cn}")

print("\nUnique Student Classes:")
for sc in Student.objects.values_list('student_class', flat=True).distinct():
    print(f"- {sc}")
