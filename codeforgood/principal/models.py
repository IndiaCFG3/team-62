from django.db import models

from django.contrib.auth.models import User
# Create your models here.
 
class Principal(models.Model):

	user = models.OneToOneField(User,on_delete=models.CASCADE)
	fid=models.CharField(max_length=10,default="#")

	def __str__(self):

		return "{} {}".format(self.user.first_name,self.user.last_name)
