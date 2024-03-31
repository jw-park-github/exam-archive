from majors_app.views import MajorsListView, MajorsDetailView, MajorsCreateView
from django.urls import path

app_name = "majors_app"

urlpatterns = [
    path('list/', MajorsListView.as_view(), name='list'),
    path('detail/<int:pk>', MajorsDetailView.as_view(), name='detail'),
    path('create/', MajorsCreateView.as_view(), name='create'),
]