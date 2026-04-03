from django.contrib.auth import get_user_model
from .models import Notification

def send_notification(user, title, message, notification_type='info', link=None):
    """
    Utility function to create a notification for a user.
    """
    return Notification.objects.create(
        user=user,
        title=title,
        message=message,
        notification_type=notification_type,
        link=link
    )

def notify_all_admins(title, message, notification_type='info', link=None):
    User = get_user_model()
    admins = User.objects.filter(is_admin=True)
    for admin in admins:
        send_notification(admin, title, message, notification_type, link)

def notify_everyone(title, message, notification_type='info', link=None):
    User = get_user_model()
    users = User.objects.all()
    for user in users:
        send_notification(user, title, message, notification_type, link)
