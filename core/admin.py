
from django.contrib import admin
from .models import Course, ContactMessage, AboutUs, FAQ, Testimonial

admin.site.register(Course)
admin.site.register(ContactMessage)
admin.site.register(AboutUs)
admin.site.register(FAQ)
admin.site.register(Testimonial)