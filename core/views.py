from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Course, ContactMessage, AboutUs, FAQ, Testimonial
from students.models import Student, Admission, Payment
from admin_panel.models import Announcements,StaffMembers
import os


def home(request):
    courses = Course.objects.all()[:6]
    testimonials = Testimonial.objects.all()[:4]
    announcements = Announcements.objects.filter(is_active=True)[:3] if 'Announcement' in globals() else []
    context = {
        'courses': courses,
        'testimonials': testimonials,
        'announcements': announcements,
    }
    return render(request, 'core/home.html', context)


def about(request):
    about = AboutUs.objects.first()
    faqs = FAQ.objects.all()
    staff = StaffMembers.objects.filter(is_active=True)[:4] if 'StaffMember' in globals() else []
    context = {
        'about': about,
        'faqs': faqs,
        'staff': staff,
    }
    return render(request, 'core/about.html', context)


def courses(request):
    courses = Course.objects.all()
    return render(request, 'core/courses.html', {'courses': courses})


def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'core/course_detail.html', {'course': course})


def download_syllabus(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if course.syllabus:
        response = HttpResponse(course.syllabus.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{course.name}_syllabus.pdf"'
        return response
    else:
        messages.error(request, 'Syllabus not available for this course.')
        return redirect('course_detail', course_id=course_id)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = ContactMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message
        )
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')

    return render(request, 'core/contact.html')


def student_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        enrollment = request.POST.get('enrollment_number')

        try:
            student = Student.objects.get(email=email)
            admission = Admission.objects.get(student=student, enrollment_number=enrollment)
            request.session['student_id'] = student.id
            messages.success(request, f'Welcome back, {student.name}!')
            return redirect('student_dashboard')
        except (Student.DoesNotExist, Admission.DoesNotExist):
            messages.error(request, 'Invalid credentials!')
            return redirect('student_login')

    return render(request, 'core/student_login.html')


def student_dashboard(request):
    if 'student_id' not in request.session:
        return redirect('student_login')

    student = get_object_or_404(Student, id=request.session['student_id'])
    admission = Admission.objects.filter(student=student).first()
    payments = Payment.objects.filter(admission=admission) if admission else []

    context = {
        'student': student,
        'admission': admission,
        'payments': payments,
    }
    return render(request, 'core/student_dashboard.html', context)


def student_logout(request):
    if 'student_id' in request.session:
        del request.session['student_id']
    messages.success(request, 'Logged out successfully!')
    return redirect('home')