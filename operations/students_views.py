from django.shortcuts import render , redirect
from .models import Student
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.db import transaction

def student(request):
    if request.method == 'POST':
        # Retrieve data from the POST request
        studentname = request.POST.get('studentname')
        mothername = request.POST.get('mothername')
        fathername = request.POST.get('fathername')
        email = request.POST.get('email')
        classA = request.POST.get('classA')
        marks = request.POST.get('marks')
        profile_picture = request.FILES.get('profilepicture')  # Handle profile picture
        print(studentname,mothername,fathername,email,classA,marks)

        # Create and save the Student object
        Student.objects.create(
            studentname=studentname,
            mothername=mothername,
            fathername=fathername,
            email=email,
            classA=classA,
            marks=marks,
            profile_picture=profile_picture
        )
        if request.POST.get('submit') == 'save':
            messages.success(request, 'Student data has been saved. You can add more students data.')
            return render(request, 'students/student.html')  # Stay on the same form page

        # If "Save and Submit" button was clicked
        if request.POST.get('submit') == 'submit':
            messages.success(request, 'Student data has been successfully submitted.')
            return redirect('student_list')  # Redirect to the employee list page

    return render(request, 'students/student.html')

def student_list(request):
    students = Student.objects.all()  # Query to get all student records
    return render(request, 'students/student-list.html', {'students': students})

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    messages.success(request, 'Student deleted successfully.')

    # Renumber the serial_number field for all remaining students
    with transaction.atomic():
        students = Student.objects.all().order_by('id')
        for index, student in enumerate(students, start=1):
            student.serial_number = index
            student.save(update_fields=['serial_number'])

    return redirect('student_list')

def update_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.studentname = request.POST.get('studentname')
        student.mothername = request.POST.get('mothername')
        student.fathername = request.POST.get('fathername')
        student.email = request.POST.get('email')
        student.classA = request.POST.get('classA')
        student.marks = request.POST.get('marks')
        if request.FILES.get('profilepicture'):
            student.profile_picture = request.FILES.get('profilepicture')
        student.save()
        messages.success(request, 'Student updated successfully.')
        return redirect('student_list')  # Adjust to your URL name for the student list

    return render(request, 'students/update-student.html', {'student': student})


def view_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/view-student.html', {'student': student})




