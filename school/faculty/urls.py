from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('teacher-dashboard/', views.teacher_dashboard, name='teacher_dashboard'),

    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/add/', views.add_teacher, name='add_teacher'),
    path('teachers/edit/<str:teacher_id>/', views.edit_teacher, name='edit_teacher'),
    path('teachers/delete/<str:teacher_id>/', views.delete_teacher, name='delete_teacher'),

    path('departments/', views.department_list, name='department_list'),
    path('departments/add/', views.add_department, name='add_department'),
    path('departments/edit/<str:department_id>/', views.edit_department, name='edit_department'),
    path('departments/delete/<str:department_id>/', views.delete_department, name='delete_department'),

    path('subjects/', views.subject_list, name='subject_list'),
    path('subjects/add/', views.add_subject, name='add_subject'),
    path('subjects/edit/<str:subject_id>/', views.edit_subject, name='edit_subject'),
    path('subjects/delete/<str:subject_id>/', views.delete_subject, name='delete_subject'),
    path('coming-soon/', views.coming_soon, name='coming_soon'),
    path('review-requests/', views.review_requests, name='review_requests'),
    path('fees/', views.fees_list, name='fees_list'),
    path('events/', views.events_list, name='events_list'),
    path('library/', views.library_list, name='book_list'),
    path('enter_grades/', views.teacher_enter_grades, name='teacher_enter_grades'),
    path('validate_grades/', views.admin_validate_grades, name='admin_validate_grades'),
    path('review_modifications/', views.teacher_review_grades, name='teacher_review_grades'),
    path('activities_board/', views.activities_board, name='activities_board'),
    path('admin-cards/', views.admin_manage_cards, name='admin_cards'),
    
    # Subject Resources (Phase 2)
    path('subjects/resources/manage/<str:subject_id>/', views.manage_subject_resources, name='manage_subject_resources'),
    path('subjects/resources/view/<str:subject_id>/', views.subject_resources, name='subject_resources'),
    path('subjects/resources/delete/<int:res_id>/', views.delete_resource, name='delete_resource'),
    path('analytics/', views.admin_advanced_analytics, name='admin_analytics'),
    
    # Assignments (Phase 4)
    path('subjects/assignments/manage/<str:subject_id>/', views.manage_assignments, name='manage_assignments'),
    path('student/assignments/', views.student_assignments, name='student_assignments'),
    path('student/assignments/submit/<int:assignment_id>/', views.submit_assignment, name='submit_assignment'),
    path('assignments/submissions/<int:assignment_id>/', views.view_submissions, name='view_submissions'),
    path('assignments/grade/<int:submission_id>/', views.grade_submission, name='grade_submission'),
]
