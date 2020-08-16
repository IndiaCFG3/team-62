from django.db import models
from teacher.models import Teacher


choices=(
    ("Male", "Male"),
    ("Female","Female")
)
# Create your models here.
class Student(models.Model):
	uid=models.CharField(max_length=10,default='#')
	name=models.CharField(max_length=50,default='#')
	gender=models.CharField(max_length=6,default='#',choices=choices)
	teacher=models.ForeignKey(Teacher,on_delete=models.DO_NOTHING)
	filled=models.BooleanField(default=False)

	def __str__ (self):

		return "{}".format(self.name)
