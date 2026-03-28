from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Student, Parent, Holiday, Exam, TimeTable
from faculty.models import Subject, Teacher

@login_required
def dashboard(request):
    if not request.user.is_student:
        return redirect('admin_dashboard') if request.user.is_admin else redirect('teacher_dashboard')
    student = Student.objects.filter(user=request.user).first()
    holidays = Holiday.objects.all()[:5]
    exams = Exam.objects.all()[:5]
    timetables = TimeTable.objects.filter(class_name=student.student_class) if student else []
    context = {'student': student, 'holidays': holidays, 'exams': exams, 'timetables': timetables}
    return render(request, 'students/student-dashboard.html', context)

@login_required
def student_list(request):
    students = Student.objects.all().order_by('student_class', 'last_name')
    class_names = Student.objects.values_list('student_class', flat=True).distinct().order_by('student_class')
    class_filter = request.GET.get('class_name', '')
    if class_filter:
        students = students.filter(student_class=class_filter)
    return render(request, 'students/students.html', {'student_list': students, 'students': students, 'class_names': class_names, 'selected_class': class_filter})

@login_required
def add_student(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        student_id = request.POST.get('student_id')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        student_class = request.POST.get('student_class')
        joining_date = request.POST.get('joining_date')
        mobile_number = request.POST.get('mobile_number')
        admission_number = request.POST.get('admission_number')
        section = request.POST.get('section')
        student_image = request.FILES.get('student_image')
        father_name = request.POST.get('father_name')
        father_occupation = request.POST.get('father_occupation')
        father_mobile = request.POST.get('father_mobile')
        father_email = request.POST.get('father_email')
        mother_name = request.POST.get('mother_name')
        mother_occupation = request.POST.get('mother_occupation')
        mother_mobile = request.POST.get('mother_mobile')
        mother_email = request.POST.get('mother_email')
        present_address = request.POST.get('present_address')
        permanent_address = request.POST.get('permanent_address')
        parent = Parent.objects.create(father_name=father_name, father_occupation=father_occupation, father_mobile=father_mobile, father_email=father_email, mother_name=mother_name, mother_occupation=mother_occupation, mother_mobile=mother_mobile, mother_email=mother_email, present_address=present_address, permanent_address=permanent_address)
        student = Student.objects.create(first_name=first_name, last_name=last_name, student_id=student_id, gender=gender, date_of_birth=date_of_birth, student_class=student_class, joining_date=joining_date, mobile_number=mobile_number, admission_number=admission_number, section=section, student_image=student_image, parent=parent)
        messages.success(request, 'Student added Successfully')
        return redirect('student_list')
    else:
        return render(request, 'students/add-student.html')

def edit_student(request, student_id):
    return render(request, 'students/edit-student.html')

def view_student(request, student_id):
    return render(request, 'students/student-details.html')

def delete_student(request, student_id):
    return redirect('student_list')

@login_required
def generate_id_card(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    return render(request, 'student/id_card.html', {'student': student})
from .models import ExamResult, CertificateRequest

@login_required
def request_certificate(request):
    if not request.user.is_student:
        return redirect('dashboard')
    student = Student.objects.filter(user=request.user).first()
    if request.method == 'POST':
        cert_type = request.POST.get('certificate_type')
        if cert_type and student:
            CertificateRequest.objects.create(student=student, certificate_type=cert_type)
            from home_auth.models import Notification, CustomUser
            admins = CustomUser.objects.filter(is_admin=True)
            for a in admins:
                Notification.objects.create(user=a, title=f"Nouvelle demande d'attestation", message=f"L'étudiant {student.first_name} {student.last_name} a demandé: {cert_type}.")
            messages.success(request, f"Votre demande de '{cert_type}' a été envoyée à l'administration.")
            return redirect('request_certificate')
    requests_history = CertificateRequest.objects.filter(student=student).order_by('-date_requested') if student else []
    return render(request, 'student/request_certificate.html', {'requests': requests_history})

@login_required
def admin_certificates(request):
    if not request.user.is_admin:
        return redirect('dashboard')
    reqs = CertificateRequest.objects.all().select_related('student').order_by('-date_requested')
    return render(request, 'student/admin_certificates.html', {'requests': reqs})

@login_required
def approve_certificate(request, req_id):
    if not request.user.is_admin:
        return redirect('dashboard')
    cert = get_object_or_404(CertificateRequest, id=req_id)
    cert.status = 'Approved'
    cert.save()
    from home_auth.models import Notification
    if cert.student.user:
        Notification.objects.create(user=cert.student.user, title='✅ Attestation Prête', message=f"Votre document officiel '{cert.certificate_type}' a été généré avec succès par la faculté.")
    messages.success(request, f"L'attestation pour {cert.student.first_name} a été générée.")
    return redirect('admin_certificates')

@login_required
def print_attestation(request, req_id):
    cert = get_object_or_404(CertificateRequest, id=req_id)
    return render(request, 'student/print_attestation.html', {'cert': cert})
from django.http import JsonResponse

@login_required
def request_student_card(request):
    if not hasattr(request.user, 'is_student') or not request.user.is_student:
        return redirect('dashboard')
    student = Student.objects.filter(user=request.user).first()
    if not student:
        return redirect('dashboard')
    from .models import StudentCardRequest
    card_req = StudentCardRequest.objects.filter(student=student).order_by('-request_date').first()
    if request.method == 'POST':
        if card_req and card_req.status in ['En attente', 'Générée']:
            from django.contrib import messages
            messages.warning(request, 'Vous avez déjà une demande en cours ou une carte validée.')
            return redirect('request_student_card')
        photo = request.FILES.get('photo')
        blood_type = request.POST.get('blood_type')
        if photo:
            StudentCardRequest.objects.create(student=student, photo=photo, blood_type=blood_type, status='En attente')
            from django.contrib import messages
            messages.success(request, "Votre demande de carte d'étudiant a été envoyée avec succès.")
            return redirect('request_student_card')
    return render(request, 'student/request_student_card.html', {'student': student, 'card_req': card_req})