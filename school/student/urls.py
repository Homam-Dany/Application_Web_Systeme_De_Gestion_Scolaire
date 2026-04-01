from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('add/', views.add_student, name='add_student'),
    path('students/<str:student_id>/', views.view_student, name='view_student'),
    path('edit/<str:student_id>/', views.edit_student, name='edit_student'),
    path('delete/<str:student_id>/', views.delete_student, name='delete_student'),

    # Holidays
    path('holidays/', views.holiday_list, name='holiday_list'),
    path('holidays/add/', views.add_holiday, name='add_holiday'),
    path('holidays/delete/<str:holiday_id>/', views.delete_holiday, name='delete_holiday'),

    # Exams
    path('exams/', views.exam_list, name='exam_list'),
    path('exams/add/', views.add_exam, name='add_exam'),
    path('exams/delete/<int:exam_id>/', views.delete_exam, name='delete_exam'),

    # TimeTable
    path('timetable/', views.timetable_list, name='timetable_list'),
    path('api/timetable/', views.api_timetable, name='api_timetable'),
    path('timetable/add/', views.add_timetable, name='add_timetable'),
    path('timetable/delete/<int:tt_id>/', views.delete_timetable, name='delete_timetable'),
    path('id/<str:student_id>/', views.generate_id_card, name='generate_id_card'),
    path('my-grades/', views.student_my_grades, name='student_my_grades'),
    path('request-certificate/', views.request_certificate, name='request_certificate'),
    path('admin-certificates/', views.admin_certificates, name='admin_certificates'),
    path('approve-certificate/<int:req_id>/', views.approve_certificate, name='approve_certificate'),
    path('print-attestation/<int:req_id>/', views.print_attestation, name='print_attestation'),
    path('request-card/', views.request_student_card, name='request_student_card'),
    
    # Temporary Class Requests
    path('timetable/request-temp/', views.request_temporary_class, name='request_temporary_class'),
    path('timetable/manage-temp/', views.admin_manage_temp_classes, name='admin_manage_temp_classes'),
    path('timetable/process-temp/<int:req_id>/', views.process_temp_class_request, name='process_temp_class_request'),
]
