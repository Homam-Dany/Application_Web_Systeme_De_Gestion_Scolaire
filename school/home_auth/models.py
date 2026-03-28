from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class AccountRequest(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    requested_role = models.CharField(max_length=20)
    status = models.CharField(max_length=20, default='Pending') # Pending, Approved, Rejected
    justification = models.TextField(blank=True, null=True)
    extra_info = models.CharField(max_length=200, blank=True, null=True)  # filiere for student, module for teacher
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.status}"

class Notification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=255)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.title}"
