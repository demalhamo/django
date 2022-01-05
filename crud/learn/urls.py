from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .models import Student
from .views import StudentAPIView, StudentDetails, FetchGet, FetchPost 
urlpatterns = [
    #path('student/', student_list),
    path('student/', StudentAPIView.as_view()),
    #path('detail/<int:pk>/', student_details),
    path('detail/<int:pk>/', StudentDetails.as_view()),

    path('fetchget/', FetchGet, ),
    path('fetchpost/', FetchPost),

]