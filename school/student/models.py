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
        return f'{self.father_name} & {self.mother_name}'

class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    date_of_birth = models.DateField()
    student_class = models.CharField(max_length=50)
    joining_date = models.DateField()
    mobile_number = models.CharField(max_length=15)
    admission_number = models.CharField(max_length=20)
    section = models.CharField(max_length=10)
    student_image = models.ImageField(upload_to='students/', blank=True)
    parent = models.OneToOneField(Parent, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.student_id})'

class CertificateRequest(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    certificate_type = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='Pending', choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')])
    date_requested = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.student} - {self.certificate_type}'

class StudentCardRequest(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='student_cards/photos/')
    blood_type = models.CharField(max_length=5, blank=True, null=True, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')])
    status = models.CharField(max_length=20, default='En attente', choices=[('En attente', 'En attente'), ('Générée', 'Générée'), ('Refusée', 'Refusée')])
    issued_card = models.FileField(upload_to='student_cards/generated/', blank=True, null=True)
    request_date = models.DateTimeField(auto_now_add=True)
    admin_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Carte {self.student.first_name} {self.student.last_name} - {self.status}'