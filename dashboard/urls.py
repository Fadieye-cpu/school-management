from django.urls import path
from . import views


app_name = 'dashboard'

urlpatterns = [
    path('etudiant/', views.student_dashboard, name='student_home'),
    path('professeur/', views.professeur_dashboard, name='prof_home'),
    path('admin-interface/', views.admin_dashboard, name='admin_home'),
]