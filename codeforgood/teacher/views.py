from django.shortcuts import render,redirect
from principal.models import Principal
from student.models import Student
from teacher.models import Teacher
from course.models import Course,Question,Response
from django.db.models import Count
import json

from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.
choices=[
    "Collaboration","Critical Thinking","Risk Taking"
]

@login_required
def home(request):
	curr_teacher=Teacher.objects.filter(user=request.user).first()
	filled_students=Student.objects.filter(filled=False,teacher=curr_teacher)
	available_students=False if len(Student.objects.filter(filled=False,teacher=curr_teacher))==0 else True
	print(filled_students)
	context={
		'students':filled_students,
		'available':available_students
	}
	return render(request,"teacher/home.html",context=context)
    

@login_required
def redirectingview(request):

	if len(Principal.objects.filter(user=request.user))!=0:
		return redirect('principal-home')

	return redirect('teacher-home')

@login_required
def visualise(request):
	curr_teacher=Teacher.objects.filter(user=request.user).first()
	answers = []
	total = []
	countList = list(Response.objects.filter(teacher=curr_teacher).values('answer').annotate(total=Count('answer')).order_by('total'))
# [{'answer': 'I have a main idea of the given presentation', 'total': 1}, {'answer': 'I share my opinions', 'total': 1}]	print(countList)
	for i in countList:
		answers.append(i["answer"])
		total.append(i["total"])
	print(answers)
	print(total)
	context = {"answers" : json.dumps(answers), "total" : json.dumps(total)}
	return render(request, "teacher/visualise.html", context = context)





@login_required
def show_questions(request,id):
	courses={}
	for course in choices:
		course_obj=Course.objects.filter(skill=course).first()
		questions=list(Question.objects.filter(course=course_obj).values_list('question',flat=True))
		courses[course]=questions
	print(courses)
	flag = True

	if request.method == 'POST':
		curr_student=Student.objects.filter(id=id).first()
		curr_teacher=Teacher.objects.filter(user=request.user).first()
		for course in courses:
			for question in courses[course]:
				checkbox=request.POST.get(question,"")
				reason=request.POST.get(question+" reason","")
				if checkbox!="":
					if reason=="":
						messages.warning(request,f'Please, Fill the description for all checked questions!')
						flag=False
					else:
						question=Question.objects.filter(question=question).first()
						response_obj=Response(question=question,teacher=curr_teacher,student=curr_student,answer=question,description=reason)
						response_obj.save()
				else:
					if reason!="":
						messages.warning(request,f'Please, Check the checkbox first!')
						flag=False
		if flag:
			curr_student.filled=True
			curr_student.save(update_fields=["filled"])
			messages.success(request,f'Your Response has been recorded!')
			return redirect('teacher-home')

	context = {
			'courses':courses
		}

	return render(request,'teacher/show_questions.html',context=context)


@login_required
def change_password(request):

	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST,user=request.user)

		if form.is_valid():
			form.save()
			update_session_auth_hash(request,form.user)
			messages.success(request,f'Your Password has been changed!')
			return redirect('redirectingurl')

		else:
			messages.warning(request,f'Your form is invalid!')
			return redirect('changepassword')

	form = PasswordChangeForm(user=request.user)
	context = {'form':form}
	return render(request,'teacher/change_password.html',context)
