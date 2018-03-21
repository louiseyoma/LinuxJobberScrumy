from django.contrib.auth.models import User, Group
from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import HttpResponseRedirect, HttpResponse
from .forms import TaskPostForm, AddUserForm, MoveTaskForm
from .models import ScrumyUser, ScrumyGoals, Rolez, Status
import random
from django.utils import timezone
from django.urls import reverse
from django.views import generic

'''
class IndexView(generic.ListView):
	template_name = 'myscrumy/test.html'

	def get_queryset(self):
		
		return ScrumyGoals.objects.all()
'''		

def index(request):
	first_user = ScrumyUser.objects.get(pk=1)
	first_user_weekly_goals = ScrumyGoals.objects.filter(user_id_id = 1, status_id_id = 4)  
	first_user_daily_goals = ScrumyGoals.objects.filter(user_id_id = 1, status_id_id = 3)
	first_user_verified_goals = ScrumyGoals.objects.filter(user_id_id = 1, status_id_id = 2)
	first_user_done_goals = ScrumyGoals.objects.filter(user_id_id = 1, status_id_id = 1)

	second_user = ScrumyUser.objects.get(pk=4)
	second_user_weekly_goals = ScrumyGoals.objects.filter(user_id_id = 2, status_id_id = 4)
	second_user_daily_goals = ScrumyGoals.objects.filter(user_id_id = 2, status_id_id = 3)
	second_user_verified_goals = ScrumyGoals.objects.filter(user_id_id = 2, status_id_id = 2)
	second_user_done_goals = ScrumyGoals.objects.filter(user_id_id = 2, status_id_id = 1)



	return render(request, 'myscrumy/home.html', {'first_user':first_user, 'wg': first_user_weekly_goals, 'dg': first_user_daily_goals, 'ver':first_user_verified_goals, 'dn':first_user_done_goals,
		'second_user':second_user, 'wg2': second_user_weekly_goals, 'dg2': second_user_daily_goals, 'ver2':second_user_verified_goals, 'dn2':second_user_done_goals} )
	
def login_page(request):

	return render(request, "myscrumy/scrum_login.html")

def add_user(request):
	if request.method == "POST":
		form = AddUserForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.role_value = Rolez.objects.get(role_value=11)
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

			a = Status.objects.get(status_id = 700)
			taskpost.status_id = a

			taskpost.time_of_status_change = timezone.now()

			taskpost.save()
			return HttpResponseRedirect('index')
	else:
		form = TaskPostForm()
	return render(request, 'myscrumy/add_task.html', {'form': form} ) 

'''
Working view for moving task
def move_task(request):
	
	if request.method == "POST":
		current_user = request.user
		current_user_group = Group.objects.get(user = current_user)
		form = MoveTaskForm(request.POST)
		if form.is_valid():
			movement = form.save(commit=False) #form details are saved in movement
			x = ScrumyGoals.objects.get(user_id_id = movement.user_id_id , task_id = movement.task_id )#search database for record with userid and taskid = values supplied in from
			x.status_id_id = movement.status_id #update statusid field in fetched record
			if movement.status_id.id == 1 or movement.status_id.id == 2:
				Regular = Group.objects.get(pk = 1)
				if current_user_group.pk == Regular.pk:
					return HttpResponseRedirect('move_task/no/permission')
				else:
					x.time_of_status_change = timezone.now()
					x.save()
					return HttpResponseRedirect('index')
			else:
				x.time_of_status_change = timezone.now()
				x.save()
				return HttpResponseRedirect('index')
	else:
		form = MoveTaskForm()
		return render(request, 'myscrumy/move_task.html',{'form': form})
'''

def move_task(request,task_id):
	
	if request.method == "POST":
		current_user = request.user
		current_user_group = Group.objects.get(user = current_user)
		x = ScrumyGoals.objects.get(task_id = task_id )#search database for record with userid and taskid = values supplied in from
		#y = request.POST.get("status")
		
		if request.POST.get("status") == 'weekly target':
			x.status_id_id = 4
			x.time_of_status_change = timezone.now()
			x.save()
			return HttpResponseRedirect(reverse('index'))
		elif request.POST.get("status") == 'daily target':
			x.status_id_id = 3
			x.time_of_status_change = timezone.now()
			x.save()
			return HttpResponseRedirect(reverse('index'))
		elif request.POST.get("status") == 'verify':
			Regular = Group.objects.get(pk = 1)
			if current_user_group.pk == Regular.pk:
				return HttpResponseRedirect(reverse('no_permission'))
			else:
				x.status_id_id = 2
				x.time_of_status_change = timezone.now()
				x.save()
				return HttpResponseRedirect(reverse('index'))
		else:
			Regular = Group.objects.get(pk = 1)
			if current_user_group.pk == Regular.pk:
				return HttpResponseRedirect(reverse('no_permission'))
			else:
				x.status_id_id = 1
				x.time_of_status_change = timezone.now()
				x.save()
				return HttpResponseRedirect(reverse('index'))
	else:
		return render(request, 'myscrumy/move_task.html')


def no_permission(request):
	#p=Group.objects.get(name = 'Regular')
	#current_user = request.user
	#current_user_group = Group.objects.filter(user = current_user)
	return render(request, "myscrumy/not_permited.html")