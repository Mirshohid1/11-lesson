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
]