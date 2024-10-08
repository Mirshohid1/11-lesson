from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('faculties/', views.faculty_list, name='faculties'),
    path('faculty_form/', views.faculty_add, name='faculty_form'),

    path('groups/', views.group_list, name='groups'),
    path('group_form/', views.group_add, name='group_form'),

    path('department_form/', views.department_add, name='department_form'),
    path('departments/', views.department_list, name='departments'),

    path('student_form/', views.student_add, name='student_form'),
    path('students/', views.student_list, name='students'),

    path('subject_form/', views.subject_add, name='subject_form'),
    path('subjects/', views.subject_list, name='subjects'),

    path('teacher/', views.teacher_add, name='teacher_form'),
    path('teachers', views.teacher_list, name='teachers'),

    path('delete_faculty/<int:pk>/', views.del_faculty, name='del_faculty'),
    path('delete_group/<int:pk>/', views.del_group, name='del_group'),
    path('delete_department/<int:pk>/', views.del_department, name='del_department'),
    path('delete_student/<int:pk>/', views.del_student, name='del_student'),
    path('delete_subject/<int:pk>/', views.del_subject, name='del_subject'),
    path('delete_teacher/<int:pk>/', views.del_teacher, name='del_teacher'),


]