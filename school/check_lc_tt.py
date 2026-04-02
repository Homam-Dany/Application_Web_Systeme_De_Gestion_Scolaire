import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school.settings')
django.setup()

from faculty.models import Teacher, Subject
from student.models import TimeTable

lc_depts = ['D06', 'LNG']
lc_teachers = Teacher.objects.filter(department__department_id__in=lc_depts)
print(f"LC Teachers headcount: {lc_teachers.count()}")

total_slots = 0
for t in lc_teachers:
    slots = TimeTable.objects.filter(teacher=t).count()
    print(f"  Teacher: {t.first_name} {t.last_name} | Slots: {slots}")
    total_slots += slots

print(f"Total LC slots in TimeTable: {total_slots}")

if total_slots == 0:
    print("WARNING: No slots found for LC teachers. Checking if they have subjects...")
    for t in lc_teachers:
        subs = Subject.objects.filter(department__department_id__in=lc_depts).count()
        print(f"  LC Subjects Available: {subs}")
        break
