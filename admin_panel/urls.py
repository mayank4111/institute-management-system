from django.urls import path
from . import views

app_name = 'admin_panel'

urlpatterns = [
    # Authentication
    path('login/', views.admin_login, name='admin_login'),
    path('logout/', views.admin_logout, name='admin_logout'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),

    # Course Management
    path('courses/', views.manage_courses, name='manage_courses'),
    path('courses/add/', views.add_course, name='add_course'),
    path('courses/<int:course_id>/edit/', views.edit_course, name='edit_course'),
    path('courses/<int:course_id>/delete/', views.delete_course, name='delete_course'),

    # Message Management
    path('messages/', views.manage_messages, name='manage_messages'),
    path('messages/<int:message_id>/', views.view_message, name='view_message'),
    path('messages/<int:message_id>/delete/', views.delete_message, name='delete_message'),

    # Admission Management
    path('admissions/', views.manage_admissions, name='manage_admissions'),
    path('admissions/<int:admission_id>/status/', views.update_admission_status, name='update_admission_status'),
    path('admissions/<int:admission_id>/payment/', views.add_payment, name='add_payment'),

    # Staff Management
    path('staff/', views.manage_staff, name='manage_staff'),
    path('staff/add/', views.add_staff, name='add_staff'),
    path('staff/<int:staff_id>/edit/', views.edit_staff, name='edit_staff'),
    path('staff/<int:staff_id>/delete/', views.delete_staff, name='delete_staff'),
]