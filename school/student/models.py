from django.db import models
from django.conf import settings

class Parent(models.Model):
    father_name = models.CharField(max_length=100)
    father_occupation = models.CharField(max_length=100, blank=True)
    father_mobile = models.CharField(max_length=15)
    father_email = models.EmailField(max_length=100)
    mother_name = models.CharField(max_length=100)
    mother_occupation = models.CharField(max_length=100, blank=True)
    mother_mobile = models.CharField(max_length=15)
    mother_email = models.EmailField(max_length=100)
    present_address = models.TextField()
    permanent_address = models.TextField()

    def __str__(self):
        return f"{self.father_name} & {self.mother_name}"

class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=[('Male','Male'), ('Female','Female')])
    date_of_birth = models.DateField()
    student_class = models.CharField(max_length=50)
    joining_date = models.DateField()
    mobile_number = models.CharField(max_length=15)
    admission_number = models.CharField(max_length=20)
    section = models.CharField(max_length=10)
    student_image = models.ImageField(upload_to='students/', blank=True)
    parent = models.OneToOneField(Parent, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.student_id})"

class Holiday(models.Model):
    holiday_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    holiday_type = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class Exam(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ForeignKey('faculty.Subject', on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    total_marks = models.IntegerField(default=20)

    def __str__(self):
        return f"{self.name} - {self.subject.name}"

class ExamResult(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2)
    proposed_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    rattrapage_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    grade = models.CharField(max_length=5, blank=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student} - {self.exam}"

class TimeTable(models.Model):
    class_name = models.CharField(max_length=50)
    section = models.CharField(max_length=10)
    subject = models.ForeignKey('faculty.Subject', on_delete=models.CASCADE)
    teacher = models.ForeignKey('faculty.Teacher', on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=20, choices=[('Monday','Monday'), ('Tuesday','Tuesday'), ('Wednesday','Wednesday'), ('Thursday','Thursday'), ('Friday','Friday'), ('Saturday','Saturday')])
    start_time = models.TimeField()
    end_time = models.TimeField()
    room_no = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.class_name} - {self.subject} ({self.day_of_week})"

class CertificateRequest(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    certificate_type = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='Pending', choices=[('Pending','Pending'), ('Approved','Approved'), ('Rejected','Rejected')])
    date_requested = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.certificate_type}"

class GradeNegotiationHistory(models.Model):
    result = models.ForeignKey(ExamResult, on_delete=models.CASCADE, related_name='negotiation_history')
    teacher = models.ForeignKey('faculty.Teacher', on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=20, choices=[('Accepté','Accepté'), ('Refusé','Refusé')])
    original_mark = models.DecimalField(max_digits=5, decimal_places=2)
    proposed_mark = models.DecimalField(max_digits=5, decimal_places=2)
    date_decided = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action} - {self.result.student} ({self.date_decided})"

class StudentCardRequest(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='student_cards/photos/')
    blood_type = models.CharField(max_length=5, blank=True, null=True, choices=[
        ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')
    ])
    status = models.CharField(max_length=20, default='En attente', choices=[
        ('En attente', 'En attente'), ('Générée', 'Générée'), ('Refusée', 'Refusée')
    ])
    issued_card = models.FileField(upload_to='student_cards/generated/', blank=True, null=True)
    request_date = models.DateTimeField(auto_now_add=True)
    admin_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Carte {self.student.first_name} {self.student.last_name} - {self.status}"

class TemporaryClassRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'In Progress'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected')
    ]
    
    REASON_CHOICES = [
        ('Rattrapage', 'Rattrapage (Catch-up)'),
        ('Soutien', 'Soutien (Support)'),
        ('Examen', 'Examen (Exam)'),
        ('Autre', 'Autre (Other)')
    ]

    teacher = models.ForeignKey('faculty.Teacher', on_delete=models.CASCADE)
    subject = models.ForeignKey('faculty.Subject', on_delete=models.CASCADE)
    class_name = models.CharField(max_length=50) # e.g. MIP
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    room_no = models.CharField(max_length=20)
    reason = models.CharField(max_length=50, choices=REASON_CHOICES)
    custom_reason = models.TextField(blank=True, null=True) # Used if reason is 'Autre'
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    admin_notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject.name} ({self.date}) - {self.status}"
