from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('operations/', login_required(views.operations), name='operations'),
    path('student/', login_required(views.student), name='student'),
    path('employee/', login_required(views.employee), name='employee'),
    path('task/',login_required(views.task),name='task'),
    path('student-list/',login_required(views.student_list),name='student_list'),
    path('task-list/',login_required(views.task_list),name='task_list'),
    path('employee-list/',login_required(views.employee_list),name='employee_list'),
    path('operations-list/',login_required(views.operations_list),name='operations_list'),
    path('delete_employee/<int:id>/', views.delete_employee, name='delete_employee'),
    path('delete_student/<int:id>/', views.delete_student, name='delete_student'),
    path('delete_operations/<int:id>/', views.delete_operations, name='delete_operations'),
    path('delete_task/<int:id>/', views.delete_task, name='delete_task'),
    path('update-employee/<int:id>/',views.update_employee, name='update_employee'),
    path('update-contact/<int:id>/',views.update_contact, name='update_contact'),
    path('update-student/<int:id>/',views.update_student, name='update_student'),
    path('update-task/<int:id>/',views.update_task, name='update_task'),
    path('index/', views.index, name='index'),
    path('view_employee/<int:pk>/', views.view_employee, name='view_employee'),
    path('view_operation/<int:pk>/', views.view_operation, name='view_operation'),
    path('view_student/<int:pk>/', views.view_student, name='view_student'),
    path('register/', views.register, name='register'),
    path('login/',views.login_view, name='login'),
    path('logout/',views.logout_view,name='logout'),
]
