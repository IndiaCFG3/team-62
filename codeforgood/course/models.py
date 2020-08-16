from django.db import models
from student.models import Student
from teacher.models import Teacher

# Create your models here.
choices=(
    ("Collaboration", "Collaboration"),
    ("Critical Thinking","Critical Thinking"),
    ("Risk Taking","Risk Taking")
)
class Course(models.Model):
	cname=models.CharField(max_length=100,default="#")
	skill=models.CharField(max_length=50,choices=choices)
	def __str__ (self):

		return "{}".format(self.cname) 



class Question(models.Model):

	course=models.ForeignKey(Course,on_delete=models.CASCADE)
	question=models.CharField(max_length=255)

	def __str__ (self):

		return "{}".format(self.question)

	# def get_absolute_url(self):
	# 	return reverse('show_questions',kwargs={'id':self.course.id})

class Response(models.Model):

	question=models.ForeignKey(Question,on_delete=models.CASCADE)
	teacher=models.ForeignKey(Teacher,on_delete=models.DO_NOTHING)
	student=models.ForeignKey(Student,on_delete=models.CASCADE)
	answer=models.CharField(max_length=255)
	description=models.CharField(max_length=255)
	bias=models.BooleanField(default=False)
    

	def __str__ (self):

		return "{} - {}".format(self.teacher.user.first_name,self.student.name)

class StudentFilledStatus(models.Model):
	# teacher=models.ForeignKey(Teacher,on_delete=models.DO_NOTHING)
	student=models.ForeignKey(Student,on_delete=models.CASCADE)
	status=models.CharField(max_length=10,default="Not Filled")

	def __str__ (self):

		return "{}".format(self.status)
