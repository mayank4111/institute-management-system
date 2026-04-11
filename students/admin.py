from django.contrib import admin
from .models import Student, Admission, Payment

# Simple registration
admin.site.register(Student)
admin.site.register(Admission)
admin.site.register(Payment)