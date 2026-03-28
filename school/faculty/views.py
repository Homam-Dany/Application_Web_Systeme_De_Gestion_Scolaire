from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Teacher, Department, Subject
from home_auth.models import CustomUser
from student.models import Student, Exam, Holiday, TimeTable

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
        dept = Department.objects.get(department_id=request.POST.get('department_id'))
        user = CustomUser.objects.create_user(
            username=request.POST.get('email'),
            email=request.POST.get('email'),
            password=request.POST.get('password'),
            is_teacher=True
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
            
        elif action == 'reject':
            acc_req.status = 'Rejected'
            acc_req.justification = justification
            acc_req.save()
            
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
                        title=f"📋 Nouvelles notes à valider : {exam.name}",
                        message=f"{request.user.first_name} {request.user.last_name} a soumis {updates_count} note(s) pour la filière {class_name}. Veuillez les vérifier dans le Bureau de Validation."
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
            from home_auth.models import Notification, CustomUser
            users = CustomUser.objects.filter(is_admin=False)
            for u in users:
                Notification.objects.create(
                    user=u,
                    title=f"📅 L'activité '{title}' a été programmée !",
                    message=f"L'administration a planifié une activité à {loc}. Résumé : {desc[:50]}..."
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
                            title=f"⚠️ Modification de Note Suggérée : {res.exam.name}",
                            message=f"L'administration propose de changer la note de {res.student.first_name} {res.student.last_name} de {res.marks_obtained} à {res.proposed_marks}. Veuillez valider dans vos Modifications Administratives."
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
                            message=f"L'administration a validé votre résultat pour l'examen '{res.exam.name}'. Score Officiel : {res.marks_obtained}/{res.exam.total_marks}."
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
                            title=f"✅ Négociation Acceptée : {res.exam.name}",
                            message=f"Le professeur a accepté votre proposition pour l'étudiant {res.student.last_name}."
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
                            title=f"❌ Négociation Refusée : {res.exam.name}",
                            message=f"Le professeur a rejeté votre proposition ({rejected_mark}) pour l'étudiant {res.student.last_name}."
                        )
                        
                    from django.contrib import messages
                    messages.warning(request, f"La proposition pour {res.student.first_name} a été refusée (note initiale conservée).")
                
                # Notify Student
                if getattr(res.student, 'user', None):
                    Notification.objects.create(
                        user=res.student.user,
                        title=f"🎓 Note Publiée : {res.exam.name}",
                        message=f"Votre résultat final pour l'examen a été publié. Score : {res.marks_obtained}/{res.exam.total_marks}."
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
            req.admin_notes = request.POST.get('rejection_reason', 'Non conforme')
            req.save()
            messages.success(request, f"La demande de {req.student.first_name} a été refusée.")
            
        elif action == 'generate':
            from PIL import Image, ImageDraw, ImageFont
            try:
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
                        student_photo = Image.open(req.photo.path)
                        student_photo = student_photo.resize((150, 200)) 
                        img.paste(student_photo, (20, 110))
                    except Exception as e:
                        pass
                        
                draw.rectangle([(0, 330), (600, 380)], fill=(240, 240, 240))
                draw.text((20, 345), "Cette carte est strictement personnelle.", fill=(100,100,100), font=font_small)
                
                fio = io.BytesIO()
                img.save(fio, format='PNG')
                fio.seek(0)
                
                filename = f"card_{s.student_id}.png"
                req.issued_card.save(filename, ContentFile(fio.read()))
                req.status = 'Générée'
                req.save()
                
                messages.success(request, f"La carte de {s.first_name} a été générée avec succès.")
            except Exception as e:
                import traceback
                traceback.print_exc()
                messages.error(request, f"Erreur de génération: {str(e)}")
                
        return redirect('admin_cards')

    requests_list = StudentCardRequest.objects.all().select_related('student').order_by('-request_date')
    return render(request, 'faculty/admin_manage_cards.html', {'requests': requests_list})
