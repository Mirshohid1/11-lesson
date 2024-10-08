from logging import fatal
from math import factorial

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import FacultyForm, GroupForm, DepartmentForm, StudentForm, SubjectForm, TeacherForm
from .models import Faculty, Group, Department, Student, Subject, Teacher


def dashboard(request):
    faculties = Faculty.objects.all()
    groups = Group.objects.all()
    departments = Department.objects.all()
    students = Student.objects.all()
    subjects = Subject.objects.all()
    teachers = Teacher.objects.all()

    return render(request, 'dashboard.html',
                  {
                      'faculties': faculties, 'groups': groups, 'departments': departments,
                      'students': students, 'subjects': subjects, 'teachers': teachers
                  })

def faculty_list(request):
    faculties = Faculty.objects.all()
    return render(request, 'faculty_list.html', {'faculties': faculties})

def faculty_add(request):
    if request.method == 'POST':
        form = FacultyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faculties')
        else:
            return HttpResponse("Form is invalid.")
    form = FacultyForm()
    ctx = {'faculty': form}
    return render(request, 'faculty_form.html', ctx)

def group_list(request):
    groups = Group.objects.all()
    return render(request, 'group_list.html', {'groups': groups})

def group_add(request):
    if request.method == 'POST':
        group = GroupForm(request.POST)
        if group.is_valid():
            group.save()
            return redirect('groups')
        else:
            return HttpResponse("Form is invalid.")
    group = GroupForm()
    ctx = {'group': group}
    return render(request, 'group_form.html', ctx)

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department_list.html', {'departments': departments})

def department_add(request):
    if request.method == 'POST':
        department = DepartmentForm(request.POST)
        if department.is_valid():
            department.save()
            return redirect('departments')
        else:
            return HttpResponse("Form is invalid.")
    department = DepartmentForm()
    ctx = {'department': department}
    return render(request, 'department_form.html', ctx)

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def student_add(request):
    if request.method == 'POST':
        student = StudentForm(request.POST)
        if student.is_valid():
            student.save()
            return redirect('groups')
        else:
            return HttpResponse("Form is invalid.")
    student = StudentForm()
    ctx = {'student': student}
    return render(request, 'student_form.html', ctx)

def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'subject_list.html', {'subjects': subjects})

def subject_add(request):
    if request.method == 'POST':
        subject = SubjectForm(request.POST)
        if subject.is_valid():
            subject.save()
            return redirect('teachers')
        else:
            return HttpResponse("Form is invalid.")
    subject = SubjectForm()
    ctx = {'subject': subject}
    return render(request, 'subject_form.html', ctx)

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher_list.html', {'teachers': teachers})

def teacher_add(request):
    if request.method == 'POST':
        teacher = TeacherForm(request.POST)
        if teacher.is_valid():
            teacher.save()
            return redirect('teachers')
        else:
            return HttpResponse("Form is invalid.")
    teacher = TeacherForm()
    ctx = {'teacher': teacher}
    return render(request, 'teacher_form.html', ctx)