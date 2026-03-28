from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('forgot-password/', views.forgot_password_view, name='forgot-password'),
    path('profile/', views.profile_view, name='profile'),
    path('api/notifications/', views.get_notifications, name='get_notifications'),
    path('api/notifications/read/<int:notif_id>/', views.mark_notification_read, name='mark_notification_read'),
    path('api/notifications/clear/', views.clear_all_notifications, name='clear_all_notifications'),
    path('api/search/', views.api_search, name='api_search'),
]
