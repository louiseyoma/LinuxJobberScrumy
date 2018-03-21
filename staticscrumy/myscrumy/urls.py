from django.conf.urls import include, url
from . import views
from django.urls import path, re_path

urlpatterns = [
    url(r'^$',views.login_page, name = 'login_page'),
    url(r'^index$',views.index, name = 'index'),
    url(r'^add_user$',views.add_user, name = 'add_user'),
    url(r'^add_task$',views.add_task, name = 'add_task'),
    #url(r'^move_task$',views.move_task, name = 'move_task'),
    #path('index',views.IndexView.as_view(), name = 'index'),
    path('move_task/<int:task_id>',views.move_task, name = 'move_task'),
    url(r'^move_task/no/permission$',views.no_permission, name = 'no_permission'),
]
