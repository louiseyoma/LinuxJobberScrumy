from django.conf.urls import include, url
from . import views
from django.urls import path, re_path

urlpatterns = [
    re_path(r'^$',views.login_page, name = 'login_page'),
    re_path(r'^index$',views.index, name = 'index'),
    re_path(r'^add_user$',views.add_user, name = 'add_user'),
    re_path(r'^add_task$',views.add_task, name = 'add_task'),
    #url(r'^move_task$',views.move_task, name = 'move_task'),
    #path('index',views.IndexView.as_view(), name = 'index'),
    path('delete/<int:task_id>',views.delete_task, name = 'delete_task'),
    path('history/<int:task_id>',views.history, name = 'history'),
    path('move_task/<int:task_id>',views.move_task, name = 'move_task'),
    re_path(r'^move_task/no/permission$',views.no_permission, name = 'no_permission'),
]
