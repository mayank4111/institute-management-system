from django.contrib import admin
from .models import AdminProfile, Announcements, StaffMembers, Event

# Simple registration
admin.site.register(AdminProfile)
admin.site.register(Announcements)
admin.site.register(StaffMembers)
admin.site.register(Event)