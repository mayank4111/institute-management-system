from django.urls import path, include
from . import views

app_name = 'core'

urlpatterns = [
    # Homepage
    path('', views.home, name='home'),

    # 🔥 ADD THESE (THIS FIXES YOUR ERROR)
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('courses/', views.courses, name='courses'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),

    # App routing
    path('students/', include('students.urls')),
    path('admin-panel/', include('admin_panel.urls')),
]
# # Media & Static (development only)
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)