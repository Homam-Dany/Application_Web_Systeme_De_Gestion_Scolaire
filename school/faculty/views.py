from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Teacher, Department, Subject, SubjectResource, Assignment, Submission
from home_auth.models import CustomUser
from home_auth.utils import send_notification
from student.models import Student, Exam, Holiday, TimeTable, ExamResult

def index(request):
    return render(request, 'authentication/login.html')

@login_required
def dashboard(request): # Student Dashboard
    student = Student.objects.filter(user=request.user).first()
    context = {
        'total_subjects': Subject.objects.filter(class_name__icontains=student.student_class).count() if student else 0,
        'total_exams': Exam.objects.filter(subject__class_name__icontains=student.student_class).count() if student else 0,
        'student_count': Student.objects.filter(student_class=student.student_class).count() if student else 0,
        'teacher_count': Subject.objects.filter(class_name__icontains=student.student_class, teacher__isnull=False).values('teacher').distinct().count() if student else 0,
        'upcoming_exams': Exam.objects.filter(subject__class_name__icontains=student.student_class).order_by('-date')[:5] if student else [],
        'holidays': Holiday.objects.all().order_by('-start_date')[:5],
        'timetables': TimeTable.objects.filter(class_name__icontains=student.student_class)[:5] if student else []
    }
    return render(request, 'students/student-dashboard.html', context)

@login_required

@login_required
def admin_dashboard(request):
    boys = Student.objects.filter(gender__iexact='Male').count()
    girls = Student.objects.filter(gender__iexact='Female').count()
    if boys == 0 and girls == 0:
        boys, girls = 55, 45 # Default visual data if db empty

    context = {
        'student_count': Student.objects.count(),
        'teacher_count': Teacher.objects.count(),
        'dept_count': Department.objects.count(),
        'subject_count': Subject.objects.count(),
        'exam_count': Exam.objects.count(),
        'holiday_count': Holiday.objects.count(),
        'boys_count': boys,
        'girls_count': girls,
        'latest_students': Student.objects.all().order_by('-id')[:5],
        'latest_teachers': Teacher.objects.all().order_by('-id')[:5]
    }
    return render(request, 'faculty/admin_dashboard.html', context)

@login_required
def teacher_dashboard(request):
    teacher = Teacher.objects.filter(user=request.user).first()
    my_subjects = Subject.objects.filter(department=teacher.department) if teacher and teacher.department else Subject.objects.none()
    student_count = Student.objects.filter(student_class__in=my_subjects.values_list('class_name', flat=True)).distinct().count()

    context = {
        'class_count': my_subjects.count(),
        'upcoming_exams': Exam.objects.filter(subject__in=my_subjects).order_by('-date')[:5],
        'student_count': student_count,
        'timetables': TimeTable.objects.filter(subject__in=my_subjects)[:5]
    }
    return render(request, 'faculty/teacher_dashboard.html', context)

@login_required
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'faculty/teachers.html', {'teachers': teachers})

@login_required
def add_teacher(request):
    departments = Department.objects.all()
    if request.method == 'POST':
        email = request.POST.get('email')
        teacher_id = request.POST.get('teacher_id')
        
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Cet email est déjà utilisé par un autre compte.')
            return render(request, 'faculty/add-teacher.html', {'departments': departments})
            
        if Teacher.objects.filter(teacher_id=teacher_id).exists():
            messages.error(request, 'Cet identifiant de formateur (ID) existe déjà.')
            return render(request, 'faculty/add-teacher.html', {'departments': departments})

        dept = Department.objects.get(department_id=request.POST.get('department_id'))
        user = CustomUser.objects.create_user(
            username=email,
            email=email,
            password=request.POST.get('password'),
            is_teacher=True,
            is_active=True  # Ensure teacher is active by default when added by admin
        )
        Teacher.objects.create(
            user=user,
            teacher_id=request.POST.get('teacher_id'),
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            gender=request.POST.get('gender'),
            mobile_number=request.POST.get('mobile_number'),
            department=dept,
            date_of_birth=request.POST.get('date_of_birth'),
            joining_date=request.POST.get('joining_date'),
            qualification=request.POST.get('qualification'),
            experience=request.POST.get('experience'),
            address=request.POST.get('address')
        )
        return redirect('teacher_list')
    return render(request, 'faculty/add-teacher.html', {'departments': departments})

@login_required
def edit_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, teacher_id=teacher_id)
    departments = Department.objects.all()
    if request.method == 'POST':
        dept = Department.objects.get(department_id=request.POST.get('department_id'))
        teacher.first_name = request.POST.get('first_name')
        teacher.last_name = request.POST.get('last_name')
        teacher.gender = request.POST.get('gender')
        teacher.mobile_number = request.POST.get('mobile_number')
        teacher.department = dept
        teacher.date_of_birth = request.POST.get('date_of_birth')
        teacher.joining_date = request.POST.get('joining_date')
        teacher.qualification = request.POST.get('qualification')
        teacher.experience = request.POST.get('experience')
        teacher.address = request.POST.get('address')
        teacher.save()
        return redirect('teacher_list')
    return render(request, 'faculty/add-teacher.html', {'teacher': teacher, 'departments': departments})

@login_required
def delete_teacher(request, teacher_id):
    if request.method == 'POST':
        teacher = get_object_or_404(Teacher, teacher_id=teacher_id)
        if teacher.user:
            teacher.user.delete()
        teacher.delete()
    return redirect('teacher_list')

@login_required
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'faculty/departments.html', {'departments': departments})

@login_required
def add_department(request):
    if request.method == 'POST':
        Department.objects.create(
            department_id=request.POST.get('department_id'),
            name=request.POST.get('name'),
            started_year=request.POST.get('started_year'),
            no_of_students=request.POST.get('no_of_students')
        )
        return redirect('department_list')
    return render(request, 'faculty/add-department.html')

@login_required
def edit_department(request, department_id):
    department = get_object_or_404(Department, department_id=department_id)
    if request.method == 'POST':
        department.name = request.POST.get('name')
        department.started_year = request.POST.get('started_year')
        department.no_of_students = request.POST.get('no_of_students')
        department.save()
        return redirect('department_list')
    return render(request, 'faculty/add-department.html', {'department': department})

@login_required
def delete_department(request, department_id):
    if request.method == 'POST':
        get_object_or_404(Department, department_id=department_id).delete()
    return redirect('department_list')

@login_required
def subject_list(request):
    if request.user.is_teacher:
        teacher = Teacher.objects.filter(user=request.user).first()
        if teacher and teacher.department:
            subjects = Subject.objects.filter(department=teacher.department).order_by('class_name', 'name')
        else:
            subjects = Subject.objects.none()
    else:
        subjects = Subject.objects.all().order_by('class_name', 'name')
    return render(request, 'faculty/subjects.html', {'subjects': subjects})

@login_required
def add_subject(request):
    departments = Department.objects.all()
    if request.method == 'POST':
        dept = Department.objects.get(department_id=request.POST.get('department_id'))
        Subject.objects.create(
            subject_id=request.POST.get('subject_id'),
            name=request.POST.get('name'),
            class_name=request.POST.get('class_name'),
            department=dept
        )
        return redirect('subject_list')
    return render(request, 'faculty/add-subject.html', {'departments': departments})

@login_required
def edit_subject(request, subject_id):
    subject = get_object_or_404(Subject, subject_id=subject_id)
    departments = Department.objects.all()
    if request.method == 'POST':
        dept = Department.objects.get(department_id=request.POST.get('department_id'))
        subject.name = request.POST.get('name')
        subject.class_name = request.POST.get('class_name')
        subject.department = dept
        subject.save()
        return redirect('subject_list')
    return render(request, 'faculty/add-subject.html', {'subject': subject, 'departments': departments})

@login_required
def delete_subject(request, subject_id):
    if request.method == 'POST':
        get_object_or_404(Subject, subject_id=subject_id).delete()
    return redirect('subject_list')

@login_required
def coming_soon(request):
    return render(request, 'faculty/coming_soon.html')

from home_auth.models import AccountRequest

@login_required
def review_requests(request):
    if not request.user.is_admin:
        return redirect('index')
        
    if request.method == 'POST':
        req_id = request.POST.get('request_id')
        action = request.POST.get('action')
        justification = request.POST.get('justification', '')
        
        acc_req = get_object_or_404(AccountRequest, id=req_id)
        
        if action == 'approve':
            acc_req.status = 'Approved'
            user = acc_req.user
            user.is_active = True
            
            import datetime
            if acc_req.requested_role.lower() == 'student':
                user.is_student = True
                
                from student.models import Student, Parent
                if not Student.objects.filter(user=user).exists():
                    parent = Parent.objects.create(
                        father_name="A compléter", father_mobile="A compléter", father_email="parent@exemple.com",
                        mother_name="A compléter", mother_mobile="A compléter", mother_email="parent2@exemple.com",
                        present_address="A compléter", permanent_address="A compléter"
                    )
                    Student.objects.create(
                        user=user,
                        first_name=user.first_name,
                        last_name=user.last_name,
                        student_id=f"STU-{user.id}",
                        gender='Male',
                        date_of_birth=datetime.date(2000, 1, 1),
                        student_class=acc_req.extra_info if acc_req.extra_info else 'Non spécifié',
                        joining_date=datetime.date.today(),
                        mobile_number="A compléter",
                        admission_number=f"ADM-{user.id}", 
                        section="A",
                        parent=parent
                    )
                    
            elif acc_req.requested_role.lower() == 'teacher':
                user.is_teacher = True
                
                from faculty.models import Teacher
                if not Teacher.objects.filter(user=user).exists():
                    Teacher.objects.create(
                        user=user,
                        first_name=user.first_name,
                        last_name=user.last_name,
                        teacher_id=f"TCH-{user.id}",
                        gender='Male',
                        date_of_birth=datetime.date(1980, 1, 1),
                        mobile_number="A compléter",
                        joining_date=datetime.date.today(),
                        qualification=acc_req.extra_info if acc_req.extra_info else 'A compléter',
                        experience="A compléter",
                        department=None,
                        address="A compléter"
                    )
                    
            elif acc_req.requested_role.lower() == 'admin':
                user.is_admin = True
                
            user.save()
            acc_req.save()
            
            # NOTIFY USER (Phase 5)
            from home_auth.utils import send_notification
            send_notification(
                user=user,
                title="🎉 Bienvenue sur Smart Campus !",
                message=f"Votre compte en tant que '{acc_req.requested_role}' a été approuvé. Connectez-vous maintenant !",
                notification_type='success',
                link='/login/'
            )
            
        elif action == 'reject':
            acc_req.status = 'Rejected'
            acc_req.justification = justification
            acc_req.save()
            
            # NOTIFY USER (Phase 5)
            from home_auth.utils import send_notification
            send_notification(
                user=acc_req.user,
                title="❌ Demande d'Inscription Refusée",
                message=f"Votre demande a été refusée par l'admin. Motif : {justification}",
                notification_type='danger',
                link='/login/'
            )
            
        return redirect('review_requests')
        
    pending_requests = AccountRequest.objects.filter(status='Pending').order_by('-created_at')
    return render(request, 'faculty/review_requests.html', {'requests': pending_requests})

from django.http import HttpResponse
def log_client_error(request):
    msg = request.GET.get('msg', '')
    print(f"!!! CLIENT SIDE JS ERROR: {msg} !!!")
    return HttpResponse('ok')


@login_required
def fees_list(request):
    return render(request, 'faculty/fees.html')

@login_required
def events_list(request):
    return render(request, 'faculty/events.html')

@login_required
def library_list(request):
    return render(request, 'faculty/library.html')

from student.models import Student, Exam, ExamResult

@login_required
def teacher_enter_grades(request):
    if not (request.user.is_teacher or request.user.is_admin):
        return redirect('dashboard')

    # POST: Save bulk grades
    if request.method == 'POST':
        exam_id = request.POST.get('exam_id')
        class_name = request.POST.get('class_name', '')
        if exam_id:
            exam = Exam.objects.get(id=exam_id)
            updates_count = 0
            for key, value in request.POST.items():
                if key.startswith('mark_') and value.strip() != '':
                    student_id = key.split('_')[1]
                    try:
                        student = Student.objects.get(id=student_id)
                        marks = float(value)
                        marks = max(0, min(20, marks))
                        ExamResult.objects.update_or_create(
                            student=student, exam=exam,
                            defaults={'marks_obtained': marks, 'grade': 'N/A', 'is_published': False}
                        )
                        updates_count += 1
                    except Exception:
                        pass
                
                if key.startswith('rat_') and value.strip() != '':
                    student_id = key.split('_')[1]
                    try:
                        student = Student.objects.get(id=student_id)
                        ratt_marks = float(value)
                        ratt_marks = max(0, min(20, ratt_marks))
                        result = ExamResult.objects.filter(student=student, exam=exam).first()
                        if result:
                            # Règle : on conserve obligatoirement la note la plus élevée
                            if float(result.marks_obtained) > ratt_marks:
                                ratt_marks = float(result.marks_obtained)
                            
                            result.rattrapage_marks = ratt_marks
                            result.is_published = False
                            result.save()
                            updates_count += 1
                    except Exception:
                        pass
            from django.contrib import messages
            from home_auth.models import Notification, CustomUser
            
            if updates_count > 0:
                # Notify Admins
                admins = CustomUser.objects.filter(is_admin=True)
                for admin in admins:
                    Notification.objects.create(
                        user=admin,
                        title=f"📋 Nouvelles notes : {exam.name}",
                        message=f"{request.user.first_name} a soumis des notes ({class_name}).",
                        notification_type='info',
                        link='/validate_grades/'
                    )
                messages.success(request, f"{updates_count} note(s) sauvegardée(s) et envoyée(s) à l'administration pour validation.")
            else:
                messages.info(request, "Aucune note n'a été modifiée ou ajoutée.")

            return redirect(f"{request.path}?class_name={class_name}&exam_id={exam_id}")

    # GET Logic
    class_name = request.GET.get('class_name', '')
    exam_id = request.GET.get('exam_id', '')

    # Build allowed classes and exams based on role
    if request.user.is_teacher:
        teacher = Teacher.objects.filter(user=request.user).first()
        # Find subjects matching the teacher's department (their academic domain)
        allowed_subjects = Subject.objects.filter(department=teacher.department) if teacher and teacher.department else Subject.objects.none()
        class_names = allowed_subjects.values_list('class_name', flat=True).distinct().order_by('class_name')
    else:
        allowed_subjects = Subject.objects.all()
        class_names = allowed_subjects.values_list('class_name', flat=True).distinct().order_by('class_name')

    # -------- EXAMS TERMINÉS (date passée, notes pas encore toutes saisies) --------
    from django.utils import timezone
    from django.db.models import Q
    today = timezone.now().date()
    now_time = timezone.now().time()

    past_exams_qs = Exam.objects.filter(
        subject__in=allowed_subjects
    ).filter(
        Q(date__lt=today) | Q(date=today, end_time__lte=now_time)
    ).select_related('subject').order_by('-date')

    # Only show exams that have at least ONE student without a grade yet
    completed_exams = []
    for ex in past_exams_qs:
        cls = ex.subject.class_name
        total_students = Student.objects.filter(student_class=cls).count()
        graded_students = ExamResult.objects.filter(exam=ex).count()
        if total_students > 0 and graded_students < total_students:
            completed_exams.append({
                'exam': ex,
                'class_name': cls,
                'total': total_students,
                'graded': graded_students,
                'missing': total_students - graded_students
            })
    # -----------------------------------------------------------------------

    selected_exam = None
    exams_for_class = []
    students_data = []

    if class_name:
        exams_for_class = Exam.objects.filter(subject__class_name=class_name, subject__in=allowed_subjects).select_related('subject')

        if exam_id:
            selected_exam = Exam.objects.filter(id=exam_id).first()
            if selected_exam:
                students = Student.objects.filter(student_class=class_name).order_by('last_name')
                results_dict = {r.student.id: r for r in ExamResult.objects.filter(exam=selected_exam)}
                for s in students:
                    res = results_dict.get(s.id)
                    if res:
                        status = "Publié" if res.is_published else "En attente (Admin)"
                        marks_val = res.marks_obtained
                    else:
                        status = "Non Saisie"
                        marks_val = ''
                    students_data.append({'student': s, 'result': res, 'status': status, 'marks': marks_val})

        all_submitted = all(d['result'] is not None for d in students_data) if students_data else False
        
        can_submit = True
        if all_submitted:
            can_submit = False
            for d in students_data:
                res = d.get('result')
                if res and float(res.marks_obtained) < 10:
                    if res.rattrapage_marks is None or not res.is_published:
                        can_submit = True
                        break

    return render(request, 'faculty/teacher_enter_grades.html', {
        'class_names': class_names,
        'selected_class': class_name,
        'exams_for_class': exams_for_class,
        'selected_exam': selected_exam,
        'students_data': students_data,
        'completed_exams': completed_exams,
        'all_submitted': all_submitted if 'all_submitted' in locals() else False,
        'can_submit': can_submit if 'can_submit' in locals() else True,
    })

@login_required
def activities_board(request):
    from .models import Activity
    if request.method == 'POST' and request.user.is_admin:
        title = request.POST.get('title')
        desc = request.POST.get('description')
        loc = request.POST.get('location')
        date = request.POST.get('date')
        if title and desc and loc and date:
            Activity.objects.create(title=title, description=desc, location=loc, date=date)
            
            # Notify Everyone (Phase 5)
            from home_auth.utils import notify_everyone
            notify_everyone(
                title=f"📅 Activité Campus : {title}",
                message=f"Nouvel événement prévu à {loc}. Venez nombreux !",
                notification_type='info',
                link='/faculty/activities_board/'
            )
            from django.contrib import messages
            messages.success(request, "Activité programmée avec succès !")
            return redirect('activities_board')
            
    activities = Activity.objects.all().order_by('-date')
    return render(request, 'faculty/activities_board.html', {'activities': activities})

@login_required
def admin_validate_grades(request):
    if not request.user.is_admin:
        return redirect('dashboard')
        
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'unpublish_all':
            class_name = request.POST.get('class_name_hidden')
            target_results = ExamResult.objects.filter(is_published=True)
            if class_name:
                target_results = target_results.filter(exam__subject__class_name=class_name)
            count = target_results.update(is_published=False)
            
            from django.contrib import messages
            messages.info(request, f"{count} notes ont été déverrouillées et peuvent être modifiées.")
            
            # Need to maintain the GET parameters on redirect
            from django.urls import reverse
            url = reverse('admin_validate_grades')
            if class_name:
                url += f"?class_name={class_name}"
            return redirect(url)
            
        if action and action.startswith('unpublish_'):
            res_id = action.split('_')[1]
            try:
                res = ExamResult.objects.get(id=res_id)
                res.is_published = False
                res.save()
                from django.contrib import messages
                messages.info(request, f"La note de {res.student.first_name} a été déverrouillée avec succès.")
            except ExamResult.DoesNotExist:
                pass
            return redirect('admin_validate_grades')
            
        result_ids = request.POST.getlist('result_ids')
        
        # Fetch all pending results that the admin might have seen on the page
        all_pending = ExamResult.objects.filter(is_published=False).select_related('exam', 'student__user')
        
        count_published = 0
        count_proposed = 0
        from home_auth.models import Notification
        
        for res in all_pending:
            new_mark_str = request.POST.get(f'marks_{res.id}')
            is_checked = str(res.id) in result_ids
            has_proposal = False
            
            if new_mark_str is not None and new_mark_str.strip() != '':
                try:
                    val = float(new_mark_str)
                    val = max(0, min(float(res.exam.total_marks), val))
                    
                    if round(float(res.marks_obtained), 2) != round(val, 2) and round(float(res.proposed_marks or -1), 2) != round(val, 2):
                        res.proposed_marks = val
                        has_proposal = True
                except ValueError:
                    pass
            
            # If the admin changed the note OR explicitly checked the box
            if has_proposal or is_checked:
                if has_proposal:
                    res.save()
                    teacher_user = None
                    try:
                        teacher_user = res.exam.subject.teacher.user
                    except AttributeError:
                        pass
                        
                    if teacher_user:
                        Notification.objects.create(
                            user=teacher_user,
                            title=f"⚠️ Modification Note : {res.exam.name}",
                            message=f"Proposition de {res.marks_obtained} -> {res.proposed_marks} pour {res.student.last_name}.",
                            notification_type='warning',
                            link='/review_modifications/'
                        )
                    count_proposed += 1
                else:
                    res.is_published = True
                    res.proposed_marks = None
                    res.save()
                    
                    if res.student.user:
                        Notification.objects.create(
                            user=res.student.user,
                            title=f"🎓 Note Publiée : {res.exam.name}",
                            message=f"Votre résultat : {res.marks_obtained}/{res.exam.total_marks}.",
                            notification_type='success',
                            link='/student/my-grades/'
                        )
                    count_published += 1
                    
        from django.contrib import messages
        if count_published > 0:
            messages.success(request, f"{count_published} note(s) validée(s) et publiée(s) aux étudiants !")
        if count_proposed > 0:
            messages.warning(request, f"{count_proposed} note(s) modifiée(s) par l'administration ont été envoyées aux professeurs pour accord.")
        return redirect('admin_validate_grades')
            
    # GET Logic
    from django.db.models import Prefetch
    from student.models import GradeNegotiationHistory
    all_results = ExamResult.objects.all().select_related('student', 'exam', 'exam__subject')
    
    # Optional filtering by class name for the admin grid
    class_filter = request.GET.get('class_name')
    if class_filter:
        all_results = all_results.filter(exam__subject__class_name=class_filter)
        
    class_names = ExamResult.objects.values_list('exam__subject__class_name', flat=True).distinct()
    
    # Group results by Exam and Session Type
    grouped_data = {}
    for res in all_results:
        key_exam = res.exam.id
        
        if not res.is_published:
            session = "Rattrapage" if res.rattrapage_marks is not None else "Normale"
        else:
            session = "Rattrapage" if res.rattrapage_marks is not None else "Normale"
            
        group_key = f"{key_exam}_{session}"
        if group_key not in grouped_data:
            grouped_data[group_key] = {
                'exam': res.exam,
                'session_name': session,
                'pending_count': 0,
                'published_count': 0,
                'results': []
            }
            
        grouped_data[group_key]['results'].append(res)
        if not res.is_published:
            grouped_data[group_key]['pending_count'] += 1
        else:
            grouped_data[group_key]['published_count'] += 1

    # Sort groups: Pending first
    groups_list = list(grouped_data.values())
    groups_list.sort(key=lambda x: (-x['pending_count'], x['exam'].subject.class_name, x['exam'].name, x['session_name']))
    
    # Check if there are any results that can be bulk approved
    has_bulk_approvable = any(group['pending_count'] > 0 for group in groups_list)
    
    history_logs = GradeNegotiationHistory.objects.all().select_related('result__student', 'result__exam', 'teacher').order_by('-date_decided')[:50]
    
    return render(request, 'faculty/admin_validate_grades.html', {
        'groups_list': groups_list,
        'has_bulk_approvable': has_bulk_approvable,
        'class_names': class_names,
        'selected_class': class_filter,
        'history_logs': history_logs
    })

@login_required
def teacher_review_grades(request):
    if not request.user.is_teacher:
        return redirect('dashboard')
        
    if request.method == 'POST':
        action = request.POST.get('action')
        result_id = request.POST.get('result_id')
        
        if result_id and action:
            res = ExamResult.objects.filter(id=result_id, proposed_marks__isnull=False).first()
            if res:
                from home_auth.models import Notification, CustomUser
                from student.models import GradeNegotiationHistory
                from .models import Teacher
                
                admins = CustomUser.objects.filter(is_admin=True)
                teacher = Teacher.objects.filter(user=request.user).first()
                original_mark = res.marks_obtained
                proposed_mark = res.proposed_marks
                
                if action == 'accept':
                    res.marks_obtained = res.proposed_marks
                    res.proposed_marks = None
                    res.is_published = True
                    res.save()
                    
                    if teacher:
                        GradeNegotiationHistory.objects.create(
                            result=res, teacher=teacher, action='Accepté',
                            original_mark=original_mark, proposed_mark=proposed_mark
                        )
                    
                    for admin in admins:
                        Notification.objects.create(
                            user=admin,
                            title=f"✅ Négociation Acceptée",
                            message=f"Modification validée pour {res.student.last_name}.",
                            notification_type='success',
                            link='/validate_grades/'
                        )
                    
                    from django.contrib import messages
                    messages.success(request, f"La modification pour {res.student.first_name} a été acceptée !")
                    
                elif action == 'reject':
                    rejected_mark = res.proposed_marks
                    res.proposed_marks = None
                    res.is_published = True
                    res.save()
                    
                    if teacher:
                        GradeNegotiationHistory.objects.create(
                            result=res, teacher=teacher, action='Refusé',
                            original_mark=original_mark, proposed_mark=proposed_mark
                        )
                    
                    for admin in admins:
                        Notification.objects.create(
                            user=admin,
                            title=f"❌ Négociation Refusée",
                            message=f"Modification rejetée pour {res.student.last_name}.",
                            notification_type='danger',
                            link='/validate_grades/'
                        )
                        
                    from django.contrib import messages
                    messages.warning(request, f"La proposition pour {res.student.first_name} a été refusée (note initiale conservée).")
                
                # Notify Student
                if getattr(res.student, 'user', None):
                    Notification.objects.create(
                        user=res.student.user,
                        title=f"🎓 Note Publiée",
                        message=f"Résultat pour {res.exam.name} : {res.marks_obtained}.",
                        notification_type='success',
                        link='/student/my-grades/'
                    )
                
        return redirect('teacher_review_grades')

    # GET logic
    from .models import Teacher
    from student.models import GradeNegotiationHistory
    teacher = Teacher.objects.filter(user=request.user).first()
    
    pending_reviews = ExamResult.objects.filter(
        proposed_marks__isnull=False,
        is_published=False,
        exam__subject__department=teacher.department
    ).select_related('student', 'exam', 'exam__subject') if teacher and teacher.department else ExamResult.objects.none()
    
    history_logs = GradeNegotiationHistory.objects.filter(teacher=teacher).order_by('-date_decided') if teacher else []
    
    return render(request, 'faculty/teacher_review_grades.html', {'pending_reviews': pending_reviews, 'history_logs': history_logs})

@login_required
def admin_manage_cards(request):
    if not hasattr(request.user, 'is_admin') or not request.user.is_admin:
        return redirect('dashboard')
        
    from student.models import StudentCardRequest
    from django.contrib import messages
    import io
    from django.core.files.base import ContentFile
    
    if request.method == 'POST':
        action = request.POST.get('action')
        req_id = request.POST.get('request_id')
        req = get_object_or_404(StudentCardRequest, id=req_id)
        
        if action == 'reject':
            req.status = 'Refusée'
            reason = request.POST.get('rejection_reason', 'Non conforme')
            req.admin_notes = reason
            req.save()
            
            # NOTIFY STUDENT
            from home_auth.utils import send_notification
            if req.student.user:
                send_notification(
                    user=req.student.user,
                    title="❌ Carte Étudiante Refusée",
                    message=f"Votre demande de carte a été refusée. Motif : {reason}",
                    notification_type='danger',
                    link='/student/cards/request/'
                )
            messages.success(request, f"La demande de {req.student.first_name} a été refusée.")
            
        elif action == 'generate':
            from PIL import Image, ImageDraw, ImageFont
            try:
                # ... [Keep previous PIL generation code exactly as is] ...
                img = Image.new('RGB', (600, 380), color=(255, 255, 255))
                draw = ImageDraw.Draw(img)
                draw.rectangle([(0, 0), (600, 80)], fill=(0, 102, 204))
                
                try:
                    font_title = ImageFont.truetype("arial.ttf", 36)
                    font_normal = ImageFont.truetype("arial.ttf", 24)
                    font_small = ImageFont.truetype("arial.ttf", 16)
                except IOError:
                    font_title = ImageFont.load_default()
                    font_normal = ImageFont.load_default()
                    font_small = ImageFont.load_default()
                
                draw.text((20, 20), "CARTE D'ÉTUDIANT", fill=(255,255,255), font=font_title)
                s = req.student
                draw.text((200, 110), f"Nom: {s.last_name.upper()}", fill=(0,0,0), font=font_normal)
                draw.text((200, 150), f"Prénom: {s.first_name.title()}", fill=(0,0,0), font=font_normal)
                draw.text((200, 190), f"Filière: {s.student_class}", fill=(0,0,0), font=font_normal)
                draw.text((200, 230), f"Faculté: Faculté des Sciences", fill=(0,0,0), font=font_normal)
                draw.text((200, 270), f"Année Univ: 2025/2026", fill=(0,0,0), font=font_normal)
                
                if req.photo:
                    try:
                        student_photo = Image.open(req.photo)
                        if student_photo.mode in ("RGBA", "P"):
                            student_photo = student_photo.convert("RGB")
                        student_photo = student_photo.resize((150, 200), Image.Resampling.LANCZOS)
                        img.paste(student_photo, (20, 110))
                    except Exception as e:
                        messages.warning(request, f"Note: La photo n'a pas pu être insérée ({str(e)}).")
                        
                draw.rectangle([(0, 330), (600, 380)], fill=(240, 240, 240))
                draw.text((20, 345), "Cette carte est strictement personnelle.", fill=(100,100,100), font=font_small)
                
                fio = io.BytesIO()
                img.save(fio, format='PNG')
                fio.seek(0)
                
                filename = f"card_{s.student_id}.png"
                req.issued_card.save(filename, ContentFile(fio.read()))
                req.status = 'Générée'
                req.save()
                
                # NOTIFY STUDENT
                from home_auth.utils import send_notification
                if req.student.user:
                    send_notification(
                        user=req.student.user,
                        title="🪪 Carte Étudiante Disponible",
                        message="Votre carte d'étudiant a été générée avec succès. Vous pouvez la consulter dans votre espace.",
                        notification_type='success',
                        link='/student/cards/request/'
                    )
                
                messages.success(request, f"La carte de {s.first_name} a été générée avec succès.")
            except Exception as e:
                import traceback
                traceback.print_exc()
                messages.error(request, f"Erreur de génération: {str(e)}")
                
        return redirect('admin_cards')

    requests_list = StudentCardRequest.objects.all().select_related('student').order_by('-request_date')
    return render(request, 'faculty/admin_manage_cards.html', {'requests': requests_list})

from .models import SubjectResource
import os

@login_required
def manage_subject_resources(request, subject_id):
    subject = get_object_or_404(Subject, subject_id=subject_id)
    
    # Check permissions (Admin or the Teacher assigned to this subject)
    is_authorized = False
    if request.user.is_admin:
        is_authorized = True
    elif request.user.is_teacher:
        teacher = Teacher.objects.filter(user=request.user).first()
        # Allow access if assigned teacher OR belongs to the same department (Phase 6)
        if subject.teacher == teacher or (teacher and teacher.department == subject.department):
            is_authorized = True
            
    if not is_authorized:
        messages.error(request, "Vous n'avez pas l'autorisation de gérer les ressources de cette matière.")
        return redirect('subject_list')

    if request.method == 'POST':
        name = request.POST.get('name')
        res_type = request.POST.get('resource_type')
        github_url = request.POST.get('github_url')
        file = request.FILES.get('file')
        
        if not name or not res_type:
            messages.error(request, "Veuillez remplir tous les champs obligatoires.")
        else:
            teacher = Teacher.objects.filter(user=request.user).first()
            
            # Validation for File
            if file:
                # 1. Size Validation (100 MB)
                if file.size > 100 * 1024 * 1024:
                    messages.error(request, "Le fichier est trop volumineux (max 100 Mo).")
                    return redirect('manage_subject_resources', subject_id=subject_id)
                
                # 2. Extension Validation (.docx only as requested)
                ext = os.path.splitext(file.name)[1].lower()
                if ext != '.docx':
                    messages.error(request, "Seuls les fichiers .docx sont autorisés par votre professeur.")
                    return redirect('manage_subject_resources', subject_id=subject_id)
            
            resource = SubjectResource.objects.create(
                subject=subject,
                name=name,
                resource_type=res_type,
                file=file,
                github_url=github_url,
                uploaded_by=teacher
            )
            
            # --- NOTIFICATION (Phase 2 Fix) ---
            # Notify all students in this class
            target_students = Student.objects.filter(student_class=subject.class_name)
            for s in target_students:
                if s.user:
                    send_notification(
                        user=s.user,
                        title=f"📚 Nouveau Cours : {subject.name}",
                        message=f"Le support '{name}' ({res_type}) est disponible.",
                        notification_type='info',
                        link=f"/subjects/resources/view/{subject.subject_id}/"
                    )
            
            messages.success(request, f"La ressource '{name}' a été ajoutée. Les {target_students.count()} étudiants de la classe ont été notifiés.")
            return redirect('manage_subject_resources', subject_id=subject_id)

    resources = subject.resources.all().order_by('-created_at')
    return render(request, 'faculty/manage_resources.html', {
        'subject': subject,
        'resources': resources
    })

@login_required
def subject_resources(request, subject_id):
    subject = get_object_or_404(Subject, subject_id=subject_id)
    resources = subject.resources.all().order_by('-created_at')
    
    return render(request, 'faculty/subject_resources.html', {
        'subject': subject,
        'resources': resources
    })

@login_required
def delete_resource(request, res_id):
    resource = get_object_or_404(SubjectResource, id=res_id)
    s_id = resource.subject.subject_id
    
    # Permission check
    if not request.user.is_admin:
        teacher = Teacher.objects.filter(user=request.user).first()
        if resource.uploaded_by != teacher:
            messages.error(request, "Action non autorisée.")
            return redirect('subject_list')
            
    resource.delete()
    messages.success(request, "Ressource supprimée.")
    return redirect('manage_subject_resources', subject_id=s_id)

@login_required
def manage_assignments(request, subject_id):
    subject = get_object_or_404(Subject, subject_id=subject_id)
    
    # Permission check
    is_authorized = False
    if request.user.is_admin:
        is_authorized = True
    elif request.user.is_teacher:
        teacher = Teacher.objects.filter(user=request.user).first()
        # Allow access if assigned teacher OR belongs to same department (Phase 6)
        if subject.teacher == teacher or (teacher and teacher.department == subject.department):
            is_authorized = True
            
    if not is_authorized:
        messages.error(request, "Accès refusé.")
        return redirect('dashboard')

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        file = request.FILES.get('file')
        github_url = request.POST.get('github_url')
        
        from django.utils import timezone
        from datetime import datetime
        
        # Convert string due_date to datetime if it's a string
        if due_date and isinstance(due_date, str):
            due_date_obj = datetime.strptime(due_date, '%Y-%m-%dT%H:%M')
            due_date_obj = timezone.make_aware(due_date_obj)
        else:
            due_date_obj = timezone.now() + timezone.timedelta(days=7) # Default if missing

        assignment = Assignment.objects.create(
            title=title,
            description=description,
            subject=subject,
            teacher=teacher,
            due_date=due_date_obj,
            file=file,
            github_url=github_url
        )
        
        # --- NOTIFICATION ENRICHIE (Phase 4.2) ---
        duration = assignment.due_date - timezone.now()
        days = duration.days
        hours = duration.seconds // 3600
        duration_str = f"{days}j {hours}h" if days > 0 else f"{hours}h"

        target_students = Student.objects.filter(student_class=subject.class_name)
        for s in target_students:
            if s.user:
                send_notification(
                    user=s.user,
                    title=f"📝 Nouveau Devoir : {subject.name}",
                    message=f"Sujet : {title}. Durée : {duration_str}. Date limite : {assignment.due_date.strftime('%d/%m %H:%M')}.",
                    notification_type='warning',
                    link="/student/assignments/"
                )
        
        messages.success(request, f"Le devoir a été publié. Durée annoncée : {duration_str}. Les {target_students.count()} étudiants ont été alertés.")
        return redirect('manage_assignments', subject_id=subject_id)

    assignments = subject.assignments.all().order_by('-created_at')
    return render(request, 'faculty/manage_assignments.html', {
        'subject': subject,
        'assignments': assignments
    })

@login_required
def student_assignments(request):
    student = Student.objects.filter(user=request.user).first()
    if not student:
        messages.error(request, "Accès réservé aux étudiants.")
        return redirect('dashboard')
    
    # Get subjects for this student class
    subjects = Subject.objects.filter(class_name=student.student_class)
    assignments = Assignment.objects.filter(subject__in=subjects).order_by('due_date')
    
    # Add submission status to assignments
    from django.utils import timezone
    for a in assignments:
        a.user_submission = Submission.objects.filter(assignment=a, student=student).first()

    return render(request, 'student/student_assignments.html', {
        'assignments': assignments,
        'student': student,
        'now': timezone.now()
    })

@login_required
def submit_assignment(request, assignment_id):
    from django.utils import timezone
    assignment = get_object_or_404(Assignment, id=assignment_id)
    student = Student.objects.filter(user=request.user).first()
    
    if request.method == 'POST':
        # --- VERIFICATION DATE LIMITE ---
        if timezone.now() > assignment.due_date:
            messages.error(request, "La date limite de dépôt est dépassée. Vous ne pouvez plus soumettre ce devoir.")
            return redirect('student_assignments')

        file = request.FILES.get('file')
        github_url = request.POST.get('github_url')
        remarks = request.POST.get('remarks')
        
        # Check if already submitted
        submission = Submission.objects.filter(assignment=assignment, student=student).first()
        if submission:
            submission.file = file or submission.file
            submission.github_url = github_url or submission.github_url
            submission.student_remarks = remarks
            submission.save()
            messages.success(request, "Votre rendu a été mis à jour.")
        else:
            Submission.objects.create(
                assignment=assignment,
                student=student,
                file=file,
                github_url=github_url,
                student_remarks=remarks
            )
            
            # NOTIFICATION for teacher
            if assignment.teacher and assignment.teacher.user:
                send_notification(
                    user=assignment.teacher.user,
                    title=f"📥 Nouveau Rendu : {assignment.title}",
                    message=f"L'étudiant {student.first_name} {student.last_name} a déposé son travail.",
                    notification_type='success',
                    link=f"/faculty/assignments/manage/{assignment.subject.subject_id}/" # To be updated with submissions view
                )
            
            messages.success(request, "Votre travail a été déposé avec succès !")
            
        return redirect('student_assignments')
    
    return redirect('student_assignments')

from django.db.models import Count, Avg, Q
from student.models import AttendanceRecord

@login_required
def admin_advanced_analytics(request):
    if not request.user.is_admin:
        return redirect('dashboard')
        
    # 1. Students per Department (Polar Area)
    depts = Department.objects.all()
    dept_stats = []
    for d in depts:
        # Link students to departments via their class_name (as defined in Subjects)
        class_names = Subject.objects.filter(department=d).values_list('class_name', flat=True).distinct()
        count = Student.objects.filter(student_class__in=class_names).count()
        dept_stats.append({'name': d.name, 'count': count or 0})

    # 2. Performance Radar (Spider) - Comparing Depts on 3 axes: Avg Grade, Attendance, Resource Count
    radar_data = {
        'labels': [d.name for d in depts[:6]], # Top 6 for readability
        'grades': [],
        'attendance': [],
        'resources': []
    }
    
    for d in depts[:6]:
        # Avg Grade
        avg_g = ExamResult.objects.filter(exam__subject__department=d).aggregate(Avg('marks_obtained'))['marks_obtained__avg'] or 12
        radar_data['grades'].append(round(float(avg_g), 1))
        
        # Attendance % (Mock/Simple calculation)
        att_count = AttendanceRecord.objects.filter(session__timetable__subject__department=d).count()
        radar_data['attendance'].append(min(100, (att_count * 2) + 70)) # Scaling for demo
        
        # Resources count
        res_count = SubjectResource.objects.filter(subject__department=d).count()
        radar_data['resources'].append(res_count * 10 or 20) # Scaling for radar (max 100)

    # 3. Success / Failure (Doughnut)
    total_res = ExamResult.objects.count()
    success = ExamResult.objects.filter(marks_obtained__gte=10).count()
    failure = total_res - success if total_res > 0 else 5

    # 4. UI Stats Items (for Glassmorphism design)
    stats_items = [
        ("Étudiants Inscrits", Student.objects.count(), "fa-users", "#22d3ee"),
        ("Corps Professoral", Teacher.objects.count(), "fa-user-tie", "#10b981"),
        ("Taux de Réussite", success, "fa-check-double", "#f59e0b"),
        ("Alertes de Risque", failure, "fa-exclamation-triangle", "#f43f5e"),
    ]

    return render(request, 'faculty/admin_analytics.html', {
        'dept_stats': dept_stats,
        'radar_data': radar_data,
        'success_count': success or 15,
        'failure_count': failure or 5,
        'total_students': Student.objects.count(),
        'total_teachers': Teacher.objects.count(),
        'stats_items': stats_items
    })

@login_required
def view_submissions(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    
    # Permission check
    is_authorized = False
    if request.user.is_admin:
        is_authorized = True
    elif request.user.is_teacher:
        teacher = Teacher.objects.filter(user=request.user).first()
        # Allow access if assigned teacher OR belongs to same dept (Phase 6)
        if assignment.subject.teacher == teacher or (teacher and teacher.department == assignment.subject.department):
            is_authorized = True
            
    if not is_authorized:
        messages.error(request, "Accès refusé.")
        return redirect('dashboard')
        
    submissions = assignment.submissions.all().select_related('student')
    
    # --- STATISTIQUES DE PARTICIPATION (Phase 4.2) ---
    total_students = Student.objects.filter(student_class=assignment.subject.class_name).count()
    submitted_count = submissions.count()
    missing_count = total_students - submitted_count
    participation_rate = round((submitted_count / total_students * 100), 1) if total_students > 0 else 0

    return render(request, 'faculty/view_submissions.html', {
        'assignment': assignment,
        'submissions': submissions,
        'stats': {
            'total': total_students,
            'submitted': submitted_count,
            'missing': missing_count,
            'rate': participation_rate
        }
    })

@login_required
def grade_submission(request, submission_id):
    submission = get_object_or_404(Submission, id=submission_id)
    
    if request.method == 'POST':
        grade = request.POST.get('grade')
        feedback = request.POST.get('feedback')
        
        try:
            submission.grade = grade
            submission.teacher_feedback = feedback
            submission.is_graded = True
            submission.save()
            
            # NOTIFICATION for student
            if submission.student.user:
                send_notification(
                    user=submission.student.user,
                    title=f"⭐ Note Disponible : {submission.assignment.title}",
                    message=f"Votre travail a été corrigé. Note : {grade}/20.",
                    notification_type='success',
                    link="/student/assignments/"
                )
            
            messages.success(request, f"Note enregistrée pour {submission.student.first_name}.")
        except Exception as e:
            messages.error(request, f"Erreur lors de l'enregistrement : {str(e)}")
            
    return redirect('view_submissions', assignment_id=submission.assignment.id)
