from subjects_app import views
from subjects_app.views import SubjectsListView
from django.urls import path, include

app_name = "subjects_app"

urlpatterns = [
    path('list/', SubjectsListView.as_view(), name='list'),
    path('level_up/', views.level_up, name='level_up'),
]