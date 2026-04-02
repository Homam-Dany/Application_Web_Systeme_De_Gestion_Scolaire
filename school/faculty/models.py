from django.db import models
from django.conf import settings

class Department(models.Model):
    department_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    started_year = models.IntegerField()
    no_of_students = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    teacher_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=[('Male','Male'), ('Female','Female')])
    date_of_birth = models.DateField()
    mobile_number = models.CharField(max_length=15)
    joining_date = models.DateField()
    qualification = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Subject(models.Model):
    subject_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class Activity(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='activities/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class SubjectResource(models.Model):
    RESOURCE_TYPES = [
        ('Cours', 'Cours / Support'),
        ('TD', 'Travaux Dirigés'),
        ('TP', 'Travaux Pratiques'),
        ('GitHub', 'Lien Projet GitHub'),
        ('Examen', 'Annales d\'Examen'),
    ]
    
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='resources')
    name = models.CharField(max_length=200)
    resource_type = models.CharField(max_length=20, choices=RESOURCE_TYPES)
    file = models.FileField(upload_to='resources/docs/', blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    uploaded_by = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject.name} - {self.name}"

class Assignment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='assignments')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    due_date = models.DateTimeField()
    file = models.FileField(upload_to='assignments/docs/', blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject.name} - {self.title}"

class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='submissions')
    student = models.ForeignKey('student.Student', on_delete=models.CASCADE)
    file = models.FileField(upload_to='submissions/docs/', blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    student_remarks = models.TextField(blank=True, null=True)
    grade = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True) # sur 20
    teacher_feedback = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_graded = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student} - {self.assignment.title}"
