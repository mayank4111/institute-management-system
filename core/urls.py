from django.urls import path, include
from . import views

urlpatterns = [
    # Homepage
    path('', views.home, name='home'),

    # App routing
    path('students/', include('students.urls')),
    path('admin-panel/', include('admin_panel.urls')),
]
# # Media & Static (development only)
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)