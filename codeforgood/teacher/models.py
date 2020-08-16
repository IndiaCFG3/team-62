from django.db import models

from django.contrib.auth.models import User
from principal.models import Principal
# Create your models here.


class Teacher(models.Model):

	user = models.OneToOneField(User,on_delete=models.CASCADE)
	fid=models.CharField(max_length=10,default="#")
	principal=models.ForeignKey(Principal,on_delete=models.DO_NOTHING)

	def __str__(self):

		return "{} {}".format(self.user.first_name,self.user.last_name)
