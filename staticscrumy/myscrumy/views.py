from django.contrib.auth.models import User, Group
from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import HttpResponseRedirect, HttpResponse
from .forms import TaskPostForm, AddUserForm, MoveTaskForm
from .models import ScrumyUser, ScrumyGoals, Status
import random
from django.utils import timezone
from django.urls import reverse
from django.views import generic
from django.core.exceptions import ObjectDoesNotExist






'''
class IndexView(generic.ListView):
	template_name = 'myscrumy/test.html'

	def get_queryset(self):
		
		return ScrumyGoals.objects.all()
'''		






def index(request):

	users = ScrumyUser.objects.all()
	
	w = []
	d = []
	v = []
	dn = []
	
	for x in range(1, users.count()+1):
		try:
			y = ScrumyUser.objects.get(id=x)
		except ObjectDoesNotExist:
			pass

		k = y.scrumygoals_set.all()

		for eachtask in k:
			if eachtask.status_id_id ==4:
				w.append(eachtask)
			elif eachtask.status_id_id ==3:
				d.append(eachtask)
			elif eachtask.status_id_id ==2:
				v.append(eachtask)
			else:
				dn.append(eachtask)


	return render(request, 'myscrumy/home.html',{'w':w,'d':d,'v':v,'dn':dn,'u':users})





	
def login_page(request):

	return render(request, "myscrumy/scrum_login.html")






def add_user(request):
	if request.method == "POST":
		form = AddUserForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.save()
			return HttpResponseRedirect('index')
	else:
		form = AddUserForm()
		return render(request, 'myscrumy/add_user.html', {'form': form} )






def add_task(request):

	if request.method == "POST":
		form = TaskPostForm(request.POST)
		if form.is_valid():
			taskpost = form.save(commit=False)

			tc = random.randint(1000,9999)
			t = ScrumyGoals.objects.filter(task_id = tc)
			if t.count():
				tc = random.randint(1000,9999)
			else:
				taskpost.task_id = tc

			a = Status.objects.get(pk = 4)
			taskpost.status_id = a

			taskpost.time_of_status_change = timezone.now()

			taskpost.created_by = request.user

			taskpost.save()
			return HttpResponseRedirect('index')
	else:
		form = TaskPostForm()
	return render(request, 'myscrumy/add_task.html', {'form': form} ) 






def history(request,task_id):
	task = ScrumyGoals.objects.get(task_id = task_id)
	if task.status_id_id == 1:
		current_status = "Done"
	elif task.status_id_id == 2:
		current_status = "Verify"
	elif task.status_id_id == 3:
		current_status = "Daily Target"
	else:
		current_status = "Weekly Target"

	if task.movement_track == 1:
		previous_status = "Done"
	elif task.movement_track == 2:
		previous_status = "Verify"
	elif task.movement_track == 3:
		previous_status = "Daily Target"
	elif task.movement_track == 4:
		previous_status = "Weekly Target"
	else:
		previous_status = "Task has never been moved"

	return HttpResponse("Last moved by: " + request.user.username + "<br>" + "from " + previous_status + " to " + current_status)






def move_task(request,task_id):
	
	if request.method == "POST":
		current_user = request.user
		current_user_group = Group.objects.get(user = current_user)
		task = ScrumyGoals.objects.get(task_id = task_id )#search database for record with userid and taskid = values supplied in from
		
		previous_status = task.status_id_id
		
		if request.POST.get("status") == 'weekly target':
			task.status_id_id = 4
			task.time_of_status_change = timezone.now()
			task.moved_by = request.user.username
			task.movement_track = previous_status
			task.save()
			return HttpResponseRedirect(reverse('index'))
		elif request.POST.get("status") == 'daily target':
			task.status_id_id = 3
			task.time_of_status_change = timezone.now()
			task.moved_by = request.user.username
			task.movement_track =  previous_status
			task.save()
			return HttpResponseRedirect(reverse('index'))
		elif request.POST.get("status") == 'verify':
			Regular = Group.objects.get(pk = 1)
			if current_user_group.pk == Regular.pk:
				return HttpResponseRedirect(reverse('no_permission'))
			else:
				task.status_id_id = 2
				task.time_of_status_change = timezone.now()
				task.moved_by = request.user.username
				task.movement_track = previous_status
				task.save()
				return HttpResponseRedirect(reverse('index'))
		else:
			Regular = Group.objects.get(pk = 1)
			if current_user_group.pk == Regular.pk:
				return HttpResponseRedirect(reverse('no_permission'))
			else:
				task.status_id_id = 1
				task.time_of_status_change = timezone.now()
				task.moved_by = request.user.username
				task.movement_track = previous_status
				task.save()
				return HttpResponseRedirect(reverse('index'))
	else:
		return render(request, 'myscrumy/move_task.html')






def no_permission(request):
	return render(request, "myscrumy/not_permited.html")






def delete_task(request,task_id):

	if request.method == "POST":
		if request.POST.get("delete") == 'yes':
			task_to_delete = ScrumyGoals.objects.get(task_id=task_id)
			task_to_delete.delete()
			return HttpResponseRedirect(reverse('index'))
		else:
			return HttpResponseRedirect(reverse('index'))	
	else:
		return render(request, "myscrumy/confirm_delete.html")

