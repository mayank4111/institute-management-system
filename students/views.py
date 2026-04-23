from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from core.models import Course
from .models import Student, Admission, Payment
import datetime


def admission_form(request):
    """Student admission form view"""
    courses = Course.objects.all()

    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        qualification = request.POST.get('qualification')
        course_id = request.POST.get('course')

        # Validation
        if not all([name, email, phone, address, gender, date_of_birth, qualification, course_id]):
            messages.error(request, 'Please fill all required fields.')
            return redirect('admission_form')

        try:
            # Check if student already exists
            student, created = Student.objects.get_or_create(
                email=email,
                defaults={
                    'name': name,
                    'phone': phone,
                    'address': address,
                    'gender': gender,
                    'date_of_birth': date_of_birth,
                    'qualification': qualification,
                    'course_id': course_id,
                    'status': 'pending'
                }
            )

            if not created:
                # Update existing student
                student.name = name
                student.phone = phone
                student.address = address
                student.gender = gender
                student.date_of_birth = date_of_birth
                student.qualification = qualification
                student.course_id = course_id
                student.save()
                messages.info(request, 'Your information has been updated.')

            # Get course
            course = get_object_or_404(Course, id=course_id)

            # Check if admission already exists
            existing_admission = Admission.objects.filter(student=student).first()
            if existing_admission:
                messages.warning(request,
                                 f'You already have an admission application. Your enrollment number is: {existing_admission.enrollment_number}')
                return redirect('admission_success', enrollment_number=existing_admission.enrollment_number)

            # Create admission
            admission = Admission.objects.create(
                student=student,
                course=course,
                fee_paid=0,
                remaining_fee=course.fee,
                status='pending'
            )

            messages.success(request,
                             f'Admission application submitted successfully! Your enrollment number is: {admission.enrollment_number}')
            return redirect('admission_success', enrollment_number=admission.enrollment_number)

        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')
            return redirect('admission_form')

    context = {
        'courses': courses,
    }
    return render(request, 'students/admission_form.html', context)


def admission_success(request, enrollment_number):
    """Admission success page view"""
    admission = get_object_or_404(Admission, enrollment_number=enrollment_number)
    return render(request, 'students/admission_success.html', {'admission': admission})


def student_list(request):
    """List all students (admin view)"""
    students = Student.objects.all().order_by('-admission_date')
    return render(request, 'students/student_list.html', {'students': students})


def student_detail(request, student_id):
    """Student detail view"""
    student = get_object_or_404(Student, id=student_id)
    admission = Admission.objects.filter(student=student).first()
    payments = Payment.objects.filter(admission=admission).order_by('-payment_date') if admission else []

    context = {
        'student': student,
        'admission': admission,
        'payments': payments,
    }
    return render(request, 'students/student_detail.html', context)


def update_student(request, student_id):
    """Update student information"""
    student = get_object_or_404(Student, id=student_id)
    courses = Course.objects.all()

    if request.method == 'POST':
        # Update student fields
        student.name = request.POST.get('name')
        student.email = request.POST.get('email')
        student.phone = request.POST.get('phone')
        student.address = request.POST.get('address')
        student.gender = request.POST.get('gender')
        student.date_of_birth = request.POST.get('date_of_birth')
        student.qualification = request.POST.get('qualification')
        student.course_id = request.POST.get('course')
        student.status = request.POST.get('status')

        # Handle photo upload
        if request.FILES.get('photo'):
            student.photo = request.FILES.get('photo')

        student.save()

        # Update admission if exists
        admission = Admission.objects.filter(student=student).first()
        if admission:
            admission.course_id = request.POST.get('course')
            admission.status = request.POST.get('status')
            admission.save()

        messages.success(request, 'Student details updated successfully!')
        return redirect('student_detail', student_id=student.id)

    context = {
        'student': student,
        'courses': courses,
    }
    return render(request, 'students/update_student.html', context)


def delete_student(request, student_id):
    """Delete student"""
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        # Delete associated admissions and payments
        admissions = Admission.objects.filter(student=student)
        for admission in admissions:
            Payment.objects.filter(admission=admission).delete()
        admissions.delete()

        # Delete student
        student.delete()

        messages.success(request, 'Student deleted successfully!')
        return redirect('student_list')

    return render(request, 'students/delete_student.html', {'student': student})