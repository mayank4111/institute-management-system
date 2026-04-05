from django.db import models
from core.models import Course
from django.contrib.auth.models import User

class Student(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('enrolled', 'Enrolled'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    qualification = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    admission_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    photo = models.ImageField(upload_to='students/', blank=True, null=True)

    def __str__(self):
        return self.name


class Admission(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    admission_date = models.DateField(auto_now_add=True)
    fee_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    remaining_fee = models.DecimalField(max_digits=10, decimal_places=2)
    enrollment_number = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=20, choices=Student.STATUS_CHOICES, default='pending')

    def save(self, *args, **kwargs):
        if not self.enrollment_number:
            import random
            import datetime
            self.enrollment_number = f"EN{datetime.datetime.now().strftime('%Y%m%d')}{random.randint(1000, 9999)}"
        if not self.remaining_fee:
            self.remaining_fee = self.course.fee - self.fee_paid
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student.name} - {self.course.name}"


class Payment(models.Model):
    admission = models.ForeignKey(Admission, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField(auto_now_add=True)
    payment_method = models.CharField(max_length=50)
    transaction_id = models.CharField(max_length=100, unique=True)
    receipt = models.FileField(upload_to='receipts/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.transaction_id:
            import random
            import datetime
            self.transaction_id = f"TXN{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}{random.randint(1000, 9999)}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.admission.student.name} - {self.amount}"