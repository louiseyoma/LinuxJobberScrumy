from django.contrib import admin

from .models import ScrumyGoals, ScrumyUser, Status, Rolez



admin.site.register(ScrumyUser)

admin.site.register(ScrumyGoals)

admin.site.register(Status)

admin.site.register(Rolez)