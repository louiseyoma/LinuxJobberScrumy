from django import forms
from django.forms import ModelForm
from .models import ScrumyGoals, ScrumyUser

class TaskPostForm(ModelForm):
	class Meta:
		model = ScrumyGoals
		fields = ['task','user_id']

class AddUserForm(ModelForm):
	class Meta:
		model = ScrumyUser
		fields = ['userName']

class MoveTaskForm(ModelForm):
	class Meta:
		model = ScrumyGoals
		fields = ['status_id', 'task_id', 'user_id']

class AssignTaskOwnerForm(ModelForm):
	class Meta:
		model = ScrumyUser
		fields = ['userName']