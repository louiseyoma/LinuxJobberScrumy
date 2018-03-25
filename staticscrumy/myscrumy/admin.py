from django.contrib import admin

from .models import ScrumyGoals, ScrumyUser, Status



admin.site.register(ScrumyUser)

admin.site.register(ScrumyGoals)

admin.site.register(Status)

