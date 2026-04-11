from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    # Admission
    path('admission/', views.admission_form, name='admission_form'),
    path('admission-success/<str:enrollment_number>/', views.admission_success, name='admission_success'),

    # Student management
    path('list/', views.student_list, name='student_list'),
    path('<int:student_id>/', views.student_detail, name='student_detail'),
    path('<int:student_id>/update/', views.update_student, name='update_student'),
    path('<int:student_id>/delete/', views.delete_student, name='delete_student'),
]