from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.show),
    path('reg/', views.register, name='reg'),
    path('all_stu/', views.all_stu, name='all_stu'),
    path('search_stu', views.search_stu, name='search_stu'),
    path('delete_stud', views.delete_stud, name='delete_stud'),
    path('delete_stud/<int:stud_id>', views.delete_stud, name='delete_stud'),
    path('update_student', views.update_student, name='update_student'),
    path('update_student/<int:id>', views.update_student, name='update_student'),
    path('Student/Update', views.STUDENT_UPDATE, name='student_update'),

]
