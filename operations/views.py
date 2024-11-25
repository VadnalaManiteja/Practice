from django.shortcuts import render
from .models import Contact,Student,Employee,Task,Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from  .decorators import role_required

# Create your views here.
def operations(request):
    if request.method == 'POST':
        # Retrieve data from the POST request
        username = request.POST.get('username')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        city = request.POST.get('city')
        pancard = request.POST.get('pancard')
        state = request.POST.get('state')
        profile_picture = request.FILES.get('profilepicture')
        # Create and save the Contact object
        Contact.objects.create(
            username=username,
            mobile=mobile,
            email=email,
            city=city,
            pancard=pancard,
            state=state,
            profile_picture=profile_picture
        )

        if request.POST.get('submit') == 'save':
            messages.success(request, 'Contact data has been saved. You can add more Contacts.')
            return render(request, 'operations.html')  # Stay on the same form page

        # If "Submit" button was clicked
        if request.POST.get('submit') == 'submit':
            messages.success(request, 'Contact data has been successfully submitted.')
            return redirect('operations_list')  # Redirect to the contact list page

    # Handle GET requests and render the form
    return render(request, 'operations.html')

@role_required('student')
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
            return render(request, 'student.html')  # Stay on the same form page

        # If "Save and Submit" button was clicked
        if request.POST.get('submit') == 'submit':
            messages.success(request, 'Student data has been successfully submitted.')
            return redirect('student_list')  # Redirect to the employee list page

    return render(request, 'student.html')

@role_required('employee')
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


def task(request):
    if request.method == 'POST':
        taskname=request.POST.get('taskname')
        startingdate=request.POST.get('startingdate')
        endingdate=request.POST.get('endingdate')
        status=request.POST.get('status')

        Task.objects.create(
            Taskname=taskname,
            Startingdate=startingdate,
            Endingdate=endingdate,
            Status=status
        )
        if request.POST.get('submit') == 'save':
            messages.success(request, 'Task data has been saved. You can add more Tasks.')
            return render(request, 'tasks.html')  # Stay on the same form page

        # If "Submit" button was clicked
        if request.POST.get('submit') == 'submit':
            messages.success(request, 'Task data has been successfully submitted.')
            return redirect('task_list')  # Redirect to the employee list page

    return render(request, 'tasks.html')


@role_required('student')
def student_list(request):
    students = Student.objects.all()  # Query to get all student records
    return render(request, 'student-list.html', {'students': students})

def task_list(request):
    tasks = Task.objects.all()  # Query to get all task records
    return render(request, 'tasks-list.html', {'tasks': tasks})

@role_required('employee')
def employee_list(request):
    employees = Employee.objects.all()  # Query to get all employee records
    return render(request, 'employee-list.html', {'employees': employees})

def operations_list(request):
    contacts = Contact.objects.all()  # Query to get all contacts records
    return render(request, 'operations-list.html', {'contacts': contacts})


from django.shortcuts import get_object_or_404, redirect
from django.db import transaction



#def delete_employee(request, id):
 #   employee = get_object_or_404(Employee, id=id)
  #  employee.delete()
   # messages.success(request, 'Employee deleted successfully.')
    #return redirect('employee_list')  # Adjust to match your list view name

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


def delete_operations(request, id):
    contact = get_object_or_404(Contact, id=id)
    contact.delete()
    messages.success(request, 'Contact deleted successfully.')

    with transaction.atomic():
        contacts = Contact.objects.all().order_by('id')
        for index, contact in enumerate(contacts, start=1):
            contact.serial_number = index
            contact.save(update_fields=['serial_number'])

    return redirect('operations_list') 

def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    messages.success(request, 'Task deleted successfully.')

    # Renumber the serial_number field for all remaining tasks
    with transaction.atomic():
        tasks = Task.objects.all().order_by('id')
        for index, task in enumerate(tasks, start=1):
            task.serial_number = index
            task.save(update_fields=['serial_number'])

    return redirect('task_list')

#def delete_task(request, id):
 #   task = get_object_or_404(Task, id=id)
  #  task.delete()
   # messages.success(request, 'Task deleted successfully.')
    #return redirect('task_list') 

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


def update_contact(request, id):
    contact = get_object_or_404(Contact, id=id)
    if request.method == 'POST':
        contact.username = request.POST.get('username')
        contact.mobile = request.POST.get('mobile')
        contact.email = request.POST.get('email')
        contact.city = request.POST.get('city')
        contact.pancard = request.POST.get('pancard')
        contact.state = request.POST.get('state')
        if 'profilepicture' in request.FILES:
            contact.profile_picture = request.FILES['profilepicture']
        contact.save()
        messages.success(request, 'Contact updated successfully.')
        return redirect('operations_list')
    return render(request, 'update-operations.html', {'contact': contact})



from django.shortcuts import render, redirect, get_object_or_404

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

    return render(request, 'update-student.html', {'student': student})


def update_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        task.Taskname = request.POST.get('taskname')  # Match the name attribute in the form
        task.Startingdate = request.POST.get('startingdate')  # Match the name attribute in the form
        task.Endingdate = request.POST.get('endingdate')  # Match the name attribute in the form
        task.Status = request.POST.get('status')  # Match the name attribute in the form
        task.save()
        messages.success(request, 'task data updated.')
        return redirect('task_list')  # Replace with the URL name for your task list

    return render(request, 'update-tasks.html', {'task': task})

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request,'index.html')

def view_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'view-employee.html', {'employee': employee})

def view_operation(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'view-operations.html', {'contact': contact})

def view_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'view-student.html', {'student': student})

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

from django.contrib import messages

from .models import Profile  # Import Profile if you're using it
ROLE_CHOICES = [
    ('employee', 'Employee'),
    ('student', 'Student'),
]

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        role = request.POST.get('role')  # Get the role from the form

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")  # Error message
        else:
            # Create the user
            user = User.objects.create_user(username=username, password=password, email=email)
            
            # Assign role to the profile (if using a Profile model)
            Profile.objects.create(user=user, role=role)  # Save the role
            
            messages.success(request, "Registration successful! You can now log in.")  # Success message
            return redirect('login')  # Redirect to the login page

    return render(request, 'register.html', {'role_choices': ROLE_CHOICES})


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(f"User logged in: {user.username}, Role: {user.profile.role}")
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password")
            
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
