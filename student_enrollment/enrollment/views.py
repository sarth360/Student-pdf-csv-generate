from django.shortcuts import render
from django.http import JsonResponse
from .forms import StudentForm
from .models import Student
import csv
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
# Create your views here.
def student_registration(request):
    form = StudentForm()
    return render(request, 'enrollment/register.html', {'form': form})

def ajax_register(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False})

def export_students_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students.csv"'

    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'Email', 'Date of Birth'])

    students = Student.objects.all().values_list('first_name', 'last_name', 'email', 'date_of_birth')
    for student in students:
        writer.writerow(student)

    return response

def export_students_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="students.pdf"'

    p = canvas.Canvas(response, pagesize=letter)
    p.setFont("Helvetica", 12)
    p.drawString(100, 750, "Student List")
    p.drawString(100, 735, "==================")

    students = Student.objects.all()
    y = 700
    for student in students:
        p.drawString(100, y, f"{student.first_name} {student.last_name} - {student.email} - {student.date_of_birth}")
        y -= 15

    p.showPage()
    p.save()
    return response