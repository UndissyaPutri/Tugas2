from django.urls import path
from todolist.views import register #sesuaikan dengan nama fungsi yang dibuat
from todolist.views import login_user #sesuaikan dengan nama fungsi yang dibuat
from todolist.views import logout_user
from todolist.views import create_task, show_todolist, delete_task
from todolist.views import update_status #sesuaikan dengan nama fungsi yang dibuat

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'), #sesuaikan dengan nama fungsi yang dibuat
    path('login/', login_user, name='login'), #sesuaikan dengan nama fungsi yang dibuat   
    path('logout/', logout_user, name='logout'), #sesuaikan dengan nama fungsi yang dibuat
    path('create-task/', create_task, name='create_task'),
    path('update-status/<int:id>', update_status, name='update_status'),
    path('delete-task/<int:id>', delete_task, name='delete_task'),
]