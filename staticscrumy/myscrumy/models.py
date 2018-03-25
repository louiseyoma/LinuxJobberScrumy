from django.db import models
from django.utils import timezone


class Status(models.Model):
	status_name = models.CharField(max_length=100)




class ScrumyUser(models.Model):
	userName = models.CharField(max_length=100)
	password = models.CharField(max_length=100, default="linuxjobber")

	def __str__(self):
		return self.userName
		

class ScrumyGoals(models.Model):
	user_id = models.ForeignKey(ScrumyUser, on_delete = models.CASCADE)
	task = models.TextField()
	task_id = models.IntegerField(default=700, null=False) # changed from charfield and null from true
	status_id = models.ForeignKey(Status, on_delete = models.PROTECT, null=False, default=700)
	time_of_status_change = models.DateTimeField(default=timezone.now, null=False)
	moved_by = models.CharField(max_length=50, default="not been moved")
	created_by = models.CharField(max_length=50, null=False)
	movement_track = models.IntegerField(default=1234, null=False)

	def __str__(self):
		return self.task