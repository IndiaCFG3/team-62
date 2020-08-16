from django.shortcuts import render
from .models import Principal
from teacher.models import Teacher
from student.models import Student
from course.models import Response,Course,Question
# Create your views here.
choices=[
    "Collaboration","Critical Thinking","Risk Taking"
]
def home(request):
    principal=Principal.objects.filter(user=request.user).first()
    all_teachers=Teacher.objects.filter(principal=principal)
    print(all_teachers)
    context={
        'teachers':all_teachers
    }
    return render(request,"principal/home.html",context=context)

def studentbyTeacher(request,id):
	curr_teacher=Teacher.objects.filter(id=id).first()
	filled_students=Student.objects.filter(teacher=curr_teacher)
	print(filled_students)
	context={
		'students':filled_students,
	}
	return render(request,"principal/homebyId.html",context=context)


def studentForm(request,id):
    student_obj=Student.objects.filter(id=id).first()

    courses={
        "Collaboration":[],"Critical Thinking":[],"Risk Taking":[],
    }
    for course in choices:
        course_obj=Course.objects.filter(skill=course).first()
        questions=list(Question.objects.filter(course=course_obj).values_list('question',flat=True))
        for question in questions:
            response_obj=Response.objects.filter(student=student_obj,answer=question).first()
            if response_obj:
                courses[course].append((question,response_obj.description))
            else:
                courses[course].append((question,""))
    print(courses)
            
        
    context={
        'courses':courses
    }
    return render(request,"principal/show_form.html",context=context)
		
		
	
    
    