from django.urls import path
from .views import *

urlpatterns = [
    path('', ToDOList.as_view(), name='home'),
    path('category/<slug:slug>/', TasksList.as_view(), name='Tasks'),
    path('task/<slug:slug>/', TaskDetail.as_view(), name='Task_detail'),
    path('complete/<int:pk>/', Complete, name='complete'),
    path('addtask', AddTaskView.as_view(), name='addtask')
]
