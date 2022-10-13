from django.urls import path
from todolist.views import add_ajax, delete_ajax, delete_task, register, show_todolist, show_todolist_ajax, data_json, login_user, logout_user, create_task, update_status

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist_ajax, name='show_todolist_ajax'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),   
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
    path('update-status/<int:id>', update_status, name='update_status'),
    path('delete-task/<int:id>', delete_ajax, name='delete_ajax'),
    path('json/', data_json, name='data_json'),
    path('add/', add_ajax, name='add_ajax'),
]