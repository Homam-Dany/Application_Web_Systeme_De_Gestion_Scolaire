from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import CustomUser, AccountRequest, Notification
from student.models import Student
from faculty.models import Teacher, Subject
from django.db.models import Q
from django.http import JsonResponse
from django.utils.timesince import timesince
from django.contrib.auth import update_session_auth_hash

def signup_view(request):
    from faculty.models import Subject
    from student.models import Student
    # Get filiere and subject options for the dynamic form
    class_names = Subject.objects.values_list('class_name', flat=True).distinct().order_by('class_name')
    subjects = Subject.objects.all().order_by('name')

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        role = request.POST.get('role')
        extra_info = request.POST.get('extra_info', '').strip()

        # Check if email exists
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Cet email est déjà utilisé.')
            return redirect('signup')

        user = CustomUser.objects.create_user(
            username=email,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            is_active=False  # Locked until admin approval
        )

        AccountRequest.objects.create(
            user=user,
            requested_role=role.capitalize(),
            status='Pending',
            extra_info=extra_info
        )

        # Notify all admins (Phase 5)
        from .utils import notify_all_admins
        notify_all_admins(
            title=f"👤 Nouvelle demande de compte",
            message=f"Rôle '{role}' demandé par {first_name} {last_name}.",
            notification_type='warning',
            link='/faculty/review-requests/'
        )

        messages.success(request, 'Inscription réussie ! Votre compte est en attente de validation par un administrateur.')
        return redirect('login')
    return render(request, 'authentication/register.html', {
        'class_names': class_names,
        'subjects': subjects
    })

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        # Check if user is pending or rejected
        inactive_user = CustomUser.objects.filter(email=email).first()
        if inactive_user and not inactive_user.is_active:
            if inactive_user.check_password(password):
                req = AccountRequest.objects.filter(user=inactive_user).first()
                if req:
                    if req.status == 'Pending':
                        messages.warning(request, 'Votre compte est toujours en attente de validation par un administrateur.')
                    elif req.status == 'Rejected':
                        reason = req.justification if req.justification else "Aucune raison fournie."
                        messages.error(request, f'Inscription refusée : {reason}')
                    return render(request, 'authentication/login.html')

        user = authenticate(request, username=email, password=password)
        
        # Dual-Login fallback: If standard username match fails, try resolving by Email
        if user is None:
            user_obj = CustomUser.objects.filter(email=email).first()
            if user_obj:
                user = authenticate(request, username=user_obj.username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Connexion réussie!')
            if user.is_admin:
                return redirect('admin_dashboard')
            elif user.is_teacher:
                return redirect('teacher_dashboard')
            elif user.is_student:
                return redirect('dashboard')
            else:
                messages.error(request, 'Rôle non défini.')
                return redirect('index')
        else:
            messages.error(request, 'Identifiants invalides.')
    return render(request, 'authentication/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Vous êtes déconnecté.')
    return redirect('index')

def forgot_password_view(request):
    return render(request, 'authentication/forgot-password.html')

@login_required
def profile_view(request):
    if request.method == 'POST':
        if 'delete_account' in request.POST:
            user = request.user
            user.delete()
            messages.success(request, 'Compte supprimé avec succès.')
            return redirect('index')
            
        request.user.first_name = request.POST.get('first_name')
        request.user.last_name = request.POST.get('last_name')
        
        new_password = request.POST.get('password')
        if new_password:
            request.user.set_password(new_password)
            update_session_auth_hash(request, request.user)
            
        request.user.save()
        messages.success(request, 'Profil mis à jour avec succès.')
        return redirect('profile')
        
    return render(request, 'authentication/profile.html')

@login_required
def get_notifications(request):
    # Fetch 5 latest unread notifications
    notifs = Notification.objects.filter(user=request.user, is_read=False).order_by('-created_at')[:5]
    data = []
    for n in notifs:
        data.append({
            'id': n.id,
            'title': n.title,
            'message': n.message,
            'time': timesince(n.created_at) + ' ago',
            'type': n.notification_type,
            'link': n.link or '#'
        })
    return JsonResponse({'count': Notification.objects.filter(user=request.user, is_read=False).count(), 'notifications': data})

@login_required
def notifications_list_view(request):
    # Retrieve all notifications for the history page
    all_notifs = Notification.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'Home/notifications_list.html', {'notifications': all_notifs})

@login_required
def mark_notification_read(request, notif_id):
    try:
        n = Notification.objects.get(id=notif_id, user=request.user)
        n.is_read = True
        n.save()
        return JsonResponse({'status': 'ok'})
    except Notification.DoesNotExist:
        return JsonResponse({'status': 'error'}, status=404)

@login_required
def clear_all_notifications(request):
    Notification.objects.filter(user=request.user, is_read=False).update(is_read=True)
    return JsonResponse({'status': 'ok'})

@login_required
def api_search(request):
    query = request.GET.get('q', '').strip()
    if not query or len(query) < 2:
        return JsonResponse({'results': []})
    
    results = []
    
    students = Student.objects.filter(
        Q(first_name__icontains=query) | 
        Q(last_name__icontains=query) | 
        Q(student_id__icontains=query)
    )[:3]
    for s in students:
        results.append({'type': 'Student', 'name': f"{s.first_name} {s.last_name}", 'id': s.student_id, 'url': f"/student/edit/{s.student_id}/"})

    teachers = Teacher.objects.filter(
        Q(first_name__icontains=query) | 
        Q(last_name__icontains=query) | 
        Q(teacher_id__icontains=query)
    )[:3]
    for t in teachers:
        results.append({'type': 'Teacher', 'name': f"{t.first_name} {t.last_name}", 'id': t.teacher_id, 'url': f"/faculty/teachers/edit/{t.teacher_id}/"})

    subjects = Subject.objects.filter(
        Q(subject_name__icontains=query) | 
        Q(subject_id__icontains=query)
    )[:3]
    for sub in subjects:
        results.append({'type': 'Subject', 'name': sub.subject_name, 'id': sub.subject_id, 'url': f"/faculty/subjects/edit/{sub.subject_id}/"})

    return JsonResponse({'results': results})
