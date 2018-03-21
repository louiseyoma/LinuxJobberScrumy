from django.db import models
from django.utils import timezone



class Rolez(models.Model):
	role_value = models.IntegerField(default=700, null=False)
	role_name = models.CharField(max_length=100)


class Status(models.Model):
	status_id =  models.IntegerField(default=700, null=False)
	status_name = models.CharField(max_length=100)




class ScrumyUser(models.Model):
	userName = models.CharField(max_length=100)
	password = models.CharField(max_length=100, default="linuxjobber")
	role_value = models.ForeignKey(Rolez, on_delete = models.PROTECT, default=11, null=False)

	def __str__(self):
		return self.userName
		

class ScrumyGoals(models.Model):
	user_id = models.ForeignKey(ScrumyUser, on_delete = models.CASCADE)
	task = models.TextField()
	task_id = models.IntegerField(default=700, null=False) # changed from charfield and null from true
	status_id = models.ForeignKey(Status, on_delete = models.PROTECT, null=False, default=700)
	time_of_status_change = models.DateTimeField(default=timezone.now, null=False)

	def __str__(self):
		return self.task