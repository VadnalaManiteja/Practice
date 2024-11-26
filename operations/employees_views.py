from django.shortcuts import render , redirect
from .models import Employee
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.db import transaction

def employee(request):
    if request.method == 'POST':
        employeeid = request.POST.get('employeeid')
        employeename = request.POST.get('employeename')
        employeeemail = request.POST.get('employeeemail')
        employeedepartment = request.POST.get('employeedepartment')
        employeeexperience = request.POST.get('employeeexperience')
        employeeskills = request.POST.get('employeeskills')
        employeesalary = request.POST.get('employeesalary')
        profile_picture = request.FILES.get('profilepicture')
        print(employeeexperience, employeesalary)

        Employee.objects.create(
            employeeid=employeeid,
            employeename=employeename,
            email=employeeemail,
            department=employeedepartment,
            experience=employeeexperience,
            skills=employeeskills,
            salary=employeesalary,
            profile_picture=profile_picture

        )
        if request.POST.get('submit') == 'save':
            messages.success(request, 'Employee data has been saved. You can add more employees.')
            return render(request, 'employee.html')  # Stay on the same form page

        # If "Submit" button was clicked
        if request.POST.get('submit') == 'submit':
            messages.success(request, 'Employee data has been successfully submitted.')
            return redirect('employee_list')  # Redirect to the employee list page

    return render(request, 'employee.html')

def employee_list(request):
    employees = Employee.objects.all()  # Query to get all employee records
    return render(request, 'employee-list.html', {'employees': employees})

def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    employee.delete()
    messages.success(request, 'Employee deleted successfully.')

    # Renumber the serial_number field for all remaining employees
    with transaction.atomic():
        employees = Employee.objects.all().order_by('id')
        for index, employee in enumerate(employees, start=1):
            employee.serial_number = index
            employee.save(update_fields=['serial_number'])

    return redirect('employee_list')

def update_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        employee.employeeid = request.POST.get('employeeid')
        employee.employeename = request.POST.get('employeename')
        employee.email = request.POST.get('email')
        employee.department = request.POST.get('department')
        employee.experience = request.POST.get('experience')
        employee.skills = request.POST.get('skills')
        employee.salary = request.POST.get('salary')
         # Handle profile picture upload
        if 'profilepicture' in request.FILES:
            employee.profile_picture = request.FILES['profilepicture']
        employee.save()
        messages.success(request, 'employee data updated')
        return redirect('employee_list')  # Adjust with your URL name for the list
    
    return render(request, 'update-employee.html', {'employee': employee})

def view_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'view-employee.html', {'employee': employee})