from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_student, name='add_student'),
    path('student-list/', views.student_list, name='student_list'),
]
