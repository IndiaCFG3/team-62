from django.shortcuts import render,redirect
from principal.models import Principal

from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.

def home(request):
    return render(request,"teacher/home.html")


def redirectingview(request):

	if len(Principal.objects.filter(user=request.user))!=0:
		return redirect('principal-home')

	return redirect('teacher-home')

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
