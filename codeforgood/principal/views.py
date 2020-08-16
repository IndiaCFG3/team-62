from django.shortcuts import render
from .models import Principal
from teacher.models import Teacher
import json
from student.models import Student
from course.models import Response,Course,Question
from django.db.models import Count

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
		
def visualise(request):
	# curr_teacher=Teacher.objects.filter(user=request.user).first()
	answers = []
	total = []
	countList = list(Response.objects.all().values('answer').annotate(total=Count('answer')).order_by('total'))
# [{'answer': 'I have a main idea of the given presentation', 'total': 1}, {'answer': 'I share my opinions', 'total': 1}]	print(countList)
	for i in countList:
		answers.append(i["answer"])
		total.append(i["total"])
	print(answers)
	print(total)
	context = {"answers" : json.dumps(answers), "total" : json.dumps(total)}
	return render(request, "principal/visualise.html", context = context)
		
	
    
    