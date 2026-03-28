from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('add/', views.add_student, name='add_student'),
    path('students/<str:student_id>/', views.view_student, name='view_student'),
    path('edit/<str:student_id>/', views.edit_student, name='edit_student'),
    path('delete/<str:student_id>/', views.delete_student, name='delete_student'),



    path('id/<str:student_id>/', views.generate_id_card, name='generate_id_card'),
    path('request-certificate/', views.request_certificate, name='request_certificate'),
    path('admin-certificates/', views.admin_certificates, name='admin_certificates'),
    path('approve-certificate/<int:req_id>/', views.approve_certificate, name='approve_certificate'),
    path('print-attestation/<int:req_id>/', views.print_attestation, name='print_attestation'),
    path('request-card/', views.request_student_card, name='request_student_card'),
]
