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

    # Calculate current average for stats
    from .models import ExamResult
    results = ExamResult.objects.filter(student=student, is_published=True)
    avg_grade = 0
    if results.exists():
        total_scaled = 0
        for r in results:
            total_m = float(r.exam.total_marks) if r.exam.total_marks else 20.0
            mark = float(r.marks_obtained)
            if r.rattrapage_marks is not None:
                mark = max(mark, float(r.rattrapage_marks))
            total_scaled += (mark / total_m) * 20.0
        avg_grade = round(total_scaled / results.count(), 2)

    context = {
        'student': student,
        'holidays': holidays,
        'exams': exams,
        'timetables': timetables,
        'average_grade': avg_grade,
        'exam_count': exams.count(),
        'total_subjects': Subject.objects.filter(class_name=student.student_class).count() if student else 0,
        'teacher_count': Subject.objects.filter(class_name=student.student_class).values('teacher').distinct().count() if student else 0
    }
    return render(request, 'students/student-dashboard.html', context)

@login_required
def student_list(request):
    students = Student.objects.all().order_by('student_class', 'last_name')
    # Get distinct class names for filière filter
    class_names = Student.objects.values_list('student_class', flat=True).distinct().order_by('student_class')
    class_filter = request.GET.get('class_name', '')
    if class_filter:
        students = students.filter(student_class=class_filter)
    return render(request, 'students/students.html', {
        'student_list': students,
        'students': students,
        'class_names': class_names,
        'selected_class': class_filter
    })

@login_required
def add_student(request):
    if not request.user.is_admin:
        return redirect('dashboard')
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

        parent = Parent.objects.create(
            father_name=father_name, father_occupation=father_occupation,
            father_mobile=father_mobile, father_email=father_email,
            mother_name=mother_name, mother_occupation=mother_occupation,
            mother_mobile=mother_mobile, mother_email=mother_email,
            present_address=present_address, permanent_address=permanent_address
        )
        student = Student.objects.create(
            first_name=first_name, last_name=last_name, student_id=student_id,
            gender=gender, date_of_birth=date_of_birth, student_class=student_class,
            joining_date=joining_date, mobile_number=mobile_number,
            admission_number=admission_number, section=section,
            student_image=student_image, parent=parent
        )
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
def holiday_list(request):
    holidays = Holiday.objects.all()
    return render(request, 'student/holidays.html', {'holidays': holidays})

@login_required
def add_holiday(request):
    if not request.user.is_admin:
        return redirect('dashboard')
    if request.method == 'POST':
        Holiday.objects.create(
            holiday_id=request.POST.get('holiday_id'),
            name=request.POST.get('name'),
            holiday_type=request.POST.get('holiday_type'),
            start_date=request.POST.get('start_date'),
            end_date=request.POST.get('end_date')
        )
        return redirect('holiday_list')
    return render(request, 'student/add-holiday.html')

@login_required
def exam_list(request):
    from django.utils import timezone
    from django.db.models import Q
    today = timezone.now().date()
    now_time = timezone.now().time()

    exams_qs = Exam.objects.all().select_related('subject').order_by('-date', '-start_time')
    
    if request.user.is_student:
        student = Student.objects.filter(user=request.user).first()
        if student:
            exams_qs = exams_qs.filter(subject__class_name__icontains=student.student_class)
    elif request.user.is_teacher:
        teacher = Teacher.objects.filter(user=request.user).first()
        if teacher and teacher.department:
            exams_qs = exams_qs.filter(subject__department=teacher.department)

    exams_data = []
    for exam in exams_qs:
        # Compute status
        if exam.date < today or (exam.date == today and exam.end_time and exam.end_time <= now_time):
            status = 'done'
            label = 'Terminé'
            badge = 'danger'
            days_left = None
        elif exam.date == today and exam.start_time and exam.start_time <= now_time:
            status = 'ongoing'
            label = 'En cours'
            badge = 'success'
            days_left = None
        else:
            delta = (exam.date - today).days
            status = 'upcoming'
            label = f'Dans {delta} jour(s)' if delta > 0 else 'Aujourd\'hui'
            badge = 'primary' if delta > 3 else 'warning'
            days_left = delta

        exams_data.append({
            'exam': exam,
            'status': status,
            'label': label,
            'badge': badge,
            'class_name': exam.subject.class_name if exam.subject else '—',
            'days_left': days_left,
        })

    return render(request, 'student/exams.html', {'exams_data': exams_data})

@login_required
def add_exam(request):
    if not (request.user.is_admin or request.user.is_teacher):
        return redirect('dashboard')
    # Logic for allowed subjects based on user role
    if request.user.is_teacher:
        teacher = Teacher.objects.filter(user=request.user).first()
        if teacher and teacher.department:
            allowed_subjects = Subject.objects.filter(department=teacher.department)
        else:
            allowed_subjects = Subject.objects.none()
    else:
        allowed_subjects = Subject.objects.all()

    # Filiere filter for subject dropdown
    class_names = allowed_subjects.values_list('class_name', flat=True).distinct().order_by('class_name')
    selected_class = request.GET.get('class_name', '') or request.POST.get('class_name', '')
    
    if selected_class:
        subjects = allowed_subjects.filter(class_name=selected_class)
    else:
        subjects = allowed_subjects

    if request.method == 'POST':
        subj = get_object_or_404(Subject, subject_id=request.POST.get('subject_id'))
        total = request.POST.get('total_marks') or 20
        exam = Exam.objects.create(
            name=request.POST.get('name'),
            subject=subj,
            date=request.POST.get('date'),
            start_time=request.POST.get('start_time'),
            end_time=request.POST.get('end_time'),
            total_marks=total
        )
        # Notify all students of this filiere
        class_name = subj.class_name
        students_in_class = Student.objects.filter(student_class=class_name)
        notif_count = 0
        from home_auth.models import Notification
        for s in students_in_class:
            if s.user:
                Notification.objects.create(
                    user=s.user,
                    title=f"📝 Nouvel examen programmé : {exam.name}",
                    message=f"Un examen de '{subj.name}' ({class_name}) a été planifié le {exam.date}. Préparez-vous !"
                )
                notif_count += 1
        from django.contrib import messages
        messages.success(request, f"Examen créé avec succès ! {notif_count} étudiant(s) notifié(s).")
        return redirect('exam_list')

    return render(request, 'student/add-exam.html', {
        'subjects': subjects,
        'class_names': class_names,
        'selected_class': selected_class,
    })

@login_required
def timetable_list(request):
    days = ['LUNDI', 'MARDI', 'MERCREDI', 'JEUDI', 'VENDREDI', 'SAMEDI']
    slots = [
        ('09:00', '10:30'),
        ('10:45', '12:15'),
        ('12:30', '14:00'),
        ('14:15', '15:45'),
        ('16:00', '17:30')
    ]
    slot_headers = [f"{s[0]} - {s[1]}" for s in slots]

    # Predefined color palettes per filiere
    filiere_colors = {
        'MIP': {'main': '#22c55e', 'border': '#16a34a', 'cell': '#dcfce7', 'header': '#15803d', 'hborder': '#166534'},
        'BCG': {'main': '#ef4444', 'border': '#dc2626', 'cell': '#fee2e2', 'header': '#b91c1c', 'hborder': '#991b1b'},
        'MIPC': {'main': '#8b5cf6', 'border': '#7c3aed', 'cell': '#ede9fe', 'header': '#6d28d9', 'hborder': '#5b21b6'},
        'GEGM': {'main': '#f97316', 'border': '#ea580c', 'cell': '#ffedd5', 'header': '#c2410c', 'hborder': '#9a3412'},
        'DEFAULT': {'main': '#3b82f6', 'border': '#2563eb', 'cell': '#eff6ff', 'header': '#1d4ed8', 'hborder': '#1e3a8a'}
    }

    def build_matrix(tts):
        matrix = {day: {f"{s[0]} - {s[1]}": [] for s in slots} for day in days}
        day_map = {
            'MONDAY': 'LUNDI', 'TUESDAY': 'MARDI', 'WEDNESDAY': 'MERCREDI',
            'THURSDAY': 'JEUDI', 'FRIDAY': 'VENDREDI', 'SATURDAY': 'SAMEDI'
        }
        for tt in tts:
            # Assign color dynamically
            base_key = tt.class_name.split('_')[0] if tt.class_name and '_' in tt.class_name else tt.class_name
            tt.colors = filiere_colors.get(base_key, filiere_colors['DEFAULT'])
            
            start_str = tt.start_time.strftime('%H:%M')
            end_str = tt.end_time.strftime('%H:%M')
            slot_key = f"{start_str} - {end_str}"
            day_str = day_map.get(tt.day_of_week.upper(), tt.day_of_week.upper())
            if day_str in matrix and slot_key in matrix[day_str]:
                matrix[day_str][slot_key].append(tt)
        
        timetable_data = []
        for day in days:
            day_row = {'day_name': day, 'slots': []}
            for s in slots:
                slot_key = f"{s[0]} - {s[1]}"
                day_row['slots'].append({'time': slot_key, 'events': matrix[day][slot_key]})
            timetable_data.append(day_row)
        return timetable_data

    context = {
        'slot_headers': slot_headers,
        'is_teacher': request.user.is_teacher,
        'is_admin': request.user.is_admin
    }

    if request.user.is_student:
        student = Student.objects.filter(user=request.user).first()
        if student and student.student_class:
            student_cls = student.student_class.lower()
            base_key = student_cls.split('_')[0].upper()
            context['table_colors'] = filiere_colors.get(base_key, filiere_colors['DEFAULT'])
            timetables = [tt for tt in TimeTable.objects.all() if tt.class_name and (student_cls in tt.class_name.lower() or tt.class_name.lower() in student_cls)]
        else:
            context['table_colors'] = filiere_colors['DEFAULT']
            timetables = []
        context['timetable_data'] = build_matrix(timetables)
        
    elif request.user.is_teacher:
        teacher = Teacher.objects.filter(user=request.user).first()
        context['table_colors'] = filiere_colors['DEFAULT']
        timetables = TimeTable.objects.filter(teacher=teacher) if teacher else []
        context['timetable_data'] = build_matrix(timetables)
        
    else:
        # Admin Global Context -> Generate matrices for ALL distinct class names
        all_timetables = TimeTable.objects.all()
        class_names = set([tt.class_name for tt in all_timetables if tt.class_name])
        
        admin_matrices = {}
        for cname in sorted(list(class_names)):
            tts = [tt for tt in all_timetables if tt.class_name == cname]
            base_key = cname.split('_')[0] if '_' in cname else cname
            color_scheme = filiere_colors.get(base_key, filiere_colors['DEFAULT'])
            admin_matrices[cname] = {
                'data': build_matrix(tts),
                'colors': color_scheme
            }
        
        context['admin_matrices'] = admin_matrices

    return render(request, 'student/timetable.html', context)

@login_required
def add_timetable(request):
    if not request.user.is_admin:
        return redirect('dashboard')
    subjects = Subject.objects.all()
    teachers = Teacher.objects.all()
    if request.method == 'POST':
        subj = get_object_or_404(Subject, subject_id=request.POST.get('subject_id'))
        teacher = get_object_or_404(Teacher, teacher_id=request.POST.get('teacher_id'))
        TimeTable.objects.create(
            class_name=request.POST.get('class_name'),
            section=request.POST.get('section'),
            subject=subj,
            teacher=teacher,
            day_of_week=request.POST.get('day_of_week'),
            start_time=request.POST.get('start_time'),
            end_time=request.POST.get('end_time'),
            room_no=request.POST.get('room_no')
        )
        return redirect('timetable_list')
    return render(request, 'student/add-timetable.html', {'subjects': subjects, 'teachers': teachers})

@login_required
def delete_holiday(request, holiday_id):
    if request.method == 'POST':
        get_object_or_404(Holiday, holiday_id=holiday_id).delete()
    return redirect('holiday_list')

@login_required
def delete_exam(request, exam_id):
    if request.method == 'POST':
        get_object_or_404(Exam, id=exam_id).delete()
    return redirect('exam_list')

@login_required
def delete_timetable(request, tt_id):
    if request.method == 'POST':
        get_object_or_404(TimeTable, id=tt_id).delete()
    return redirect('timetable_list')

@login_required
def generate_id_card(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    return render(request, 'student/id_card.html', {'student': student})

from .models import ExamResult, CertificateRequest

@login_required
def student_my_grades(request):
    if not request.user.is_student:
        return redirect('dashboard')
    
    student = Student.objects.filter(user=request.user).first()
    if not student:
        return render(request, 'student/student_grades.html', {'grouped_results': {}})
        
    results = ExamResult.objects.filter(student=student, is_published=True).select_related('exam', 'exam__subject').order_by('exam__subject__class_name', 'exam__date')
    
    # Structure for the Relevé de Notes:
    # {
    #   'MIP_S1': { 'results': [..], 'total': sum, 'count': count, 'average': avg, 'status': 'VALIDÉ'/'NON VALIDÉ' }
    # }
    grouped_results = {}
    for r in results:
        cname = r.exam.subject.class_name if r.exam.subject else "Général"
        if cname not in grouped_results:
            grouped_results[cname] = {'results': [], 'sum_marks': 0.0, 'count': 0, 'has_rat': False, 'has_nv': False}
            
        total_m = float(r.exam.total_marks) if r.exam.total_marks else 20.0
        
        # Calculate Normal Note and Rattrapage Note scaled to 20
        note_normale_scaled = (float(r.marks_obtained) / total_m) * 20.0
        
        note_rattrapage_scaled = None
        if r.rattrapage_marks is not None:
            note_rattrapage_scaled = (float(r.rattrapage_marks) / total_m) * 20.0
            
        final_mark = note_normale_scaled
        if note_rattrapage_scaled is not None:
            final_mark = max(note_normale_scaled, note_rattrapage_scaled)
            
        # Initial status before compensation
        status = 'RAT'
        if final_mark >= 10:
            status = 'V'
        elif 7 <= final_mark < 10:
            if note_rattrapage_scaled is None:
                status = 'RAT'
                grouped_results[cname]['has_rat'] = True
            else:
                status = 'VC_ELIGIBLE' # Will check for average >= 10 later
        else: # final_mark < 7
            if note_rattrapage_scaled is None:
                status = 'RAT'
                grouped_results[cname]['has_rat'] = True
            else:
                status = 'NV'
                grouped_results[cname]['has_nv'] = True
        
        grouped_results[cname]['results'].append({
            'element': r.exam.subject.name.upper(),
            'exam_name': r.exam.name,
            'note': r.marks_obtained,
            'note_rattrapage': r.rattrapage_marks,
            'total_marks': r.exam.total_marks,
            'final_mark': final_mark,
            'status': status
        })
        grouped_results[cname]['sum_marks'] += final_mark
        grouped_results[cname]['count'] += 1

    # Pass 2: Calculate averages and assign VC / Final Statuses
    for cname, data in grouped_results.items():
        avg = data['sum_marks'] / data['count'] if data['count'] > 0 else 0
        data['average'] = round(avg, 3)
        
        semester_status = 'NON VALIDÉ'
        if not data['has_rat'] and not data['has_nv'] and avg >= 10:
            semester_status = 'VALIDÉ'
            
        data['semester_status'] = semester_status
        
        # Resolve VC_ELIGIBLE based on semester average
        for res in data['results']:
            if res['status'] == 'VC_ELIGIBLE':
                res['status'] = 'VC' if avg >= 10 and not data['has_nv'] else 'NV'

    return render(request, 'student/student_grades.html', {
        'grouped_results': grouped_results, 
        'student': student
    })


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
                Notification.objects.create(
                    user=a,
                    title=f"Nouvelle demande d'attestation",
                    message=f"L'étudiant {student.first_name} {student.last_name} a demandé: {cert_type}."
                )
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
        Notification.objects.create(
            user=cert.student.user,
            title="✅ Attestation Prête",
            message=f"Votre document officiel '{cert.certificate_type}' a été généré avec succès par la faculté."
        )
    messages.success(request, f"L'attestation pour {cert.student.first_name} a été générée.")
    return redirect('admin_certificates')

@login_required
def print_attestation(request, req_id):
    cert = get_object_or_404(CertificateRequest, id=req_id)
    return render(request, 'student/print_attestation.html', {'cert': cert})

from django.http import JsonResponse
@login_required
def api_timetable(request):
    tts = TimeTable.objects.all()
    if hasattr(request.user, 'is_student') and request.user.is_student:
        from student.models import Student
        student = Student.objects.filter(user=request.user).first()
        if student and student.student_class:
            student_cls = student.student_class.lower()
            tts = [tt for tt in tts if tt.class_name and (student_cls in tt.class_name.lower() or tt.class_name.lower() in student_cls)]
        else:
            tts = []
            
    events = []
    colors = ['#007bff', '#28a745', '#dc3545', '#f39c12', '#17a2b8', '#6610f2', '#e83e8c', '#34495e']
    day_map = {'Sunday': 0, 'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6}
    
    for tt in tts:
        color_idx = len(tt.subject.name) % len(colors)
        events.append({
            'title': f"{tt.subject.name}\n{tt.room_no}",
            'daysOfWeek': [day_map.get(tt.day_of_week, 1)],
            'startTime': str(tt.start_time),
            'endTime': str(tt.end_time),
            'backgroundColor': colors[color_idx],
            'borderColor': colors[color_idx],
        })
    return JsonResponse(events, safe=False)

@login_required
def request_student_card(request):
    if not hasattr(request.user, 'is_student') or not request.user.is_student:
        return redirect('dashboard')
        
    student = Student.objects.filter(user=request.user).first()
    if not student:
        return redirect('dashboard')
        
    from .models import StudentCardRequest
    # Get the latest request
    card_req = StudentCardRequest.objects.filter(student=student).order_by('-request_date').first()
    
    if request.method == 'POST':
        # If there's already a pending or generated request, don't allow a new one
        if card_req and card_req.status in ['En attente', 'Générée']:
            from django.contrib import messages
            messages.warning(request, "Vous avez déjà une demande en cours ou une carte validée.")
            return redirect('request_student_card')
            
        photo = request.FILES.get('photo')
        blood_type = request.POST.get('blood_type')
        
        if photo:
            StudentCardRequest.objects.create(
                student=student,
                photo=photo,
                blood_type=blood_type,
                status='En attente'
            )
            from django.contrib import messages
            messages.success(request, "Votre demande de carte d'étudiant a été envoyée avec succès.")
            return redirect('request_student_card')
            
    return render(request, 'student/request_student_card.html', {
        'student': student,
        'card_req': card_req
    })
