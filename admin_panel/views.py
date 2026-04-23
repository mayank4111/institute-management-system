from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from core.models import Course, ContactMessage, AboutUs, FAQ, Testimonial
from students.models import Student, Admission, Payment
from .models import AdminProfile, Announcements, StaffMembers, Event
import os


def admin_login(request):
    """Admin login view"""
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('admin_dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user and user.is_staff:
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Invalid credentials or you do not have admin privileges.')

    return render(request, 'admin_panel/login.html')


@login_required
def admin_dashboard(request):
    """Admin dashboard view"""
    if not request.user.is_staff:
        return redirect('admin_login')

    # Statistics
    total_students = Student.objects.count()
    total_courses = Course.objects.count()
    pending_admissions = Admission.objects.filter(status='pending').count()
    total_messages = ContactMessage.objects.filter(is_read=False).count()
    total_staff = StaffMembers.objects.count()
    total_earnings = sum([admission.fee_paid for admission in Admission.objects.all()])

    # Recent data
    recent_students = Student.objects.order_by('-admission_date')[:5]
    recent_messages = ContactMessage.objects.order_by('-created_at')[:5]
    recent_admissions = Admission.objects.order_by('-admission_date')[:5]

    context = {
        'total_students': total_students,
        'total_courses': total_courses,
        'pending_admissions': pending_admissions,
        'total_messages': total_messages,
        'total_staff': total_staff,
        'total_earnings': total_earnings,
        'recent_students': recent_students,
        'recent_messages': recent_messages,
        'recent_admissions': recent_admissions,
    }
    return render(request, 'admin_panel/dashboard.html', context)


# Course Management Views
@login_required
def manage_courses(request):
    """Manage courses view"""
    if not request.user.is_staff:
        return redirect('admin_login')

    courses = Course.objects.all().order_by('-created_at')
    return render(request, 'admin_panel/manage_courses.html', {'courses': courses})


@login_required
def add_course(request):
    """Add new course view"""
    if not request.user.is_staff:
        return redirect('admin_login')

    if request.method == 'POST':
        name = request.POST.get('name')
        category = request.POST.get('category')
        duration = request.POST.get('duration')
        fee = request.POST.get('fee')
        description = request.POST.get('description')
        syllabus = request.FILES.get('syllabus')
        image = request.FILES.get('image')

        # Validation
        if not all([name, category, duration, fee, description]):
            messages.error(request, 'Please fill all required fields.')
            return redirect('add_course')

        try:
            course = Course.objects.create(
                name=name,
                category=category,
                duration=duration,
                fee=fee,
                description=description,
                syllabus=syllabus,
                image=image
            )
            messages.success(request, f'Course "{course.name}" added successfully!')
            return redirect('manage_courses')
        except Exception as e:
            messages.error(request, f'Error adding course: {str(e)}')
            return redirect('add_course')

    return render(request, 'admin_panel/add_course.html')


@login_required
def edit_course(request, course_id):
    """Edit course view"""
    if not request.user.is_staff:
        return redirect('admin_login')

    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        course.name = request.POST.get('name')
        course.category = request.POST.get('category')
        course.duration = request.POST.get('duration')
        course.fee = request.POST.get('fee')
        course.description = request.POST.get('description')

        # Handle file uploads
        if request.FILES.get('syllabus'):
            if course.syllabus and os.path.isfile(course.syllabus.path):
                os.remove(course.syllabus.path)
            course.syllabus = request.FILES.get('syllabus')

        if request.FILES.get('image'):
            if course.image and os.path.isfile(course.image.path):
                os.remove(course.image.path)
            course.image = request.FILES.get('image')

        course.save()
        messages.success(request, f'Course "{course.name}" updated successfully!')
        return redirect('manage_courses')

    return render(request, 'admin_panel/edit_course.html', {'course': course})


@login_required
def delete_course(request, course_id):
    """Delete course view"""
    if not request.user.is_staff:
        return redirect('admin_login')

    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        # Delete associated files
        if course.syllabus and os.path.isfile(course.syllabus.path):
            os.remove(course.syllabus.path)
        if course.image and os.path.isfile(course.image.path):
            os.remove(course.image.path)

        course_name = course.name
        course.delete()
        messages.success(request, f'Course "{course_name}" deleted successfully!')
        return redirect('manage_courses')

    return render(request, 'admin_panel/delete_course.html', {'course': course})


# Message Management Views
@login_required
def manage_messages(request):
    """Manage contact messages view"""
    if not request.user.is_staff:
        return redirect('admin_login')

    messages_list = ContactMessage.objects.all().order_by('-created_at')
    return render(request, 'admin_panel/manage_messages.html', {'messages': messages_list})


@login_required
def view_message(request, message_id):
    """View single message"""
    if not request.user.is_staff:
        return redirect('admin_login')

    message = get_object_or_404(ContactMessage, id=message_id)
    message.is_read = True
    message.save()

    return render(request, 'admin_panel/view_message.html', {'message': message})


@login_required
def delete_message(request, message_id):
    """Delete message"""
    if not request.user.is_staff:
        return redirect('admin_login')

    message = get_object_or_404(ContactMessage, id=message_id)

    if request.method == 'POST':
        message.delete()
        messages.success(request, 'Message deleted successfully!')
        return redirect('manage_messages')

    return render(request, 'admin_panel/delete_message.html', {'message': message})


# Admission Management Views
@login_required
def manage_admissions(request):
    """Manage admissions view"""
    if not request.user.is_staff:
        return redirect('admin_login')

    admissions = Admission.objects.all().order_by('-admission_date')
    return render(request, 'admin_panel/manage_admissions.html', {'admissions': admissions})


@login_required
def update_admission_status(request, admission_id):
    """Update admission status"""
    if not request.user.is_staff:
        return redirect('admin_login')

    admission = get_object_or_404(Admission, id=admission_id)

    if request.method == 'POST':
        new_status = request.POST.get('status')
        admission.status = new_status
        admission.save()

        # Update student status
        admission.student.status = new_status
        admission.student.save()

        messages.success(request, f'Admission status updated to {new_status}!')
        return redirect('manage_admissions')

    return render(request, 'admin_panel/update_admission_status.html', {'admission': admission})


@login_required
def add_payment(request, admission_id):
    """Add payment for admission"""
    if not request.user.is_staff:
        return redirect('admin_login')

    admission = get_object_or_404(Admission, id=admission_id)

    if request.method == 'POST':
        amount = float(request.POST.get('amount', 0))
        payment_method = request.POST.get('payment_method')
        receipt = request.FILES.get('receipt')

        if amount <= 0:
            messages.error(request, 'Please enter a valid amount.')
            return redirect('add_payment', admission_id=admission_id)

        if amount > admission.remaining_fee:
            messages.error(request, f'Amount cannot exceed remaining fee of ₹{admission.remaining_fee}')
            return redirect('add_payment', admission_id=admission_id)

        try:
            # Create payment record
            payment = Payment.objects.create(
                admission=admission,
                amount=amount,
                payment_method=payment_method,
                receipt=receipt
            )

            # Update admission fees
            admission.fee_paid += amount
            admission.remaining_fee = admission.course.fee - admission.fee_paid
            admission.save()

            messages.success(request,
                             f'Payment of ₹{amount} added successfully! Transaction ID: {payment.transaction_id}')
            return redirect('manage_admissions')

        except Exception as e:
            messages.error(request, f'Error adding payment: {str(e)}')
            return redirect('add_payment', admission_id=admission_id)

    return render(request, 'admin_panel/add_payment.html', {'admission': admission})


# Staff Management Views
@login_required
def manage_staff(request):
    """Manage staff members view"""
    if not request.user.is_staff:
        return redirect('admin_login')

    staff_members = StaffMembers.objects.all().order_by('-is_active', 'name')
    return render(request, 'admin_panel/manage_staff.html', {'staff_members': staff_members})


@login_required
def add_staff(request):
    """Add new staff member"""
    if not request.user.is_staff:
        return redirect('admin_login')

    if request.method == 'POST':
        name = request.POST.get('name')
        designation = request.POST.get('designation')
        qualification = request.POST.get('qualification')
        experience = request.POST.get('experience')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        bio = request.POST.get('bio')
        photo = request.FILES.get('photo')

        # Validation
        if not all([name, designation, qualification, experience, email, phone, bio]):
            messages.error(request, 'Please fill all required fields.')
            return redirect('add_staff')

        try:
            staff = StaffMembers.objects.create(
                name=name,
                designation=designation,
                qualification=qualification,
                experience=experience,
                email=email,
                phone=phone,
                bio=bio,
                photo=photo,
                is_active=True
            )
            messages.success(request, f'Staff member "{staff.name}" added successfully!')
            return redirect('manage_staff')
        except Exception as e:
            messages.error(request, f'Error adding staff: {str(e)}')
            return redirect('add_staff')

    return render(request, 'admin_panel/add_staff.html')


@login_required
def edit_staff(request, staff_id):
    """Edit staff member"""
    if not request.user.is_staff:
        return redirect('admin_login')

    staff = get_object_or_404(StaffMembers, id=staff_id)

    if request.method == 'POST':
        staff.name = request.POST.get('name')
        staff.designation = request.POST.get('designation')
        staff.qualification = request.POST.get('qualification')
        staff.experience = request.POST.get('experience')
        staff.email = request.POST.get('email')
        staff.phone = request.POST.get('phone')
        staff.bio = request.POST.get('bio')
        staff.is_active = request.POST.get('is_active') == 'on'

        if request.FILES.get('photo'):
            if staff.photo and os.path.isfile(staff.photo.path):
                os.remove(staff.photo.path)
            staff.photo = request.FILES.get('photo')

        staff.save()
        messages.success(request, f'Staff member "{staff.name}" updated successfully!')
        return redirect('manage_staff')

    return render(request, 'admin_panel/edit_staff.html', {'staff': staff})


@login_required
def delete_staff(request, staff_id):
    """Delete staff member"""
    if not request.user.is_staff:
        return redirect('admin_login')

    staff = get_object_or_404(StaffMembers, id=staff_id)

    if request.method == 'POST':
        if staff.photo and os.path.isfile(staff.photo.path):
            os.remove(staff.photo.path)
        staff_name = staff.name
        staff.delete()
        messages.success(request, f'Staff member "{staff_name}" deleted successfully!')
        return redirect('manage_staff')

    return render(request, 'admin_panel/delete_staff.html', {'staff': staff})


@login_required
def admin_logout(request):
    """Admin logout view"""
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('admin_login')