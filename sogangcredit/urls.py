from django.contrib import admin
from django.urls import path, include


from majors_app.views import MajorsListView
from subjects_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MajorsListView.as_view(), name='home'),
    path('subjects/', include('subjects_app.urls')),
    path('accounts/', include('accounts_app.urls')),
    path('majors/', include('majors_app.urls')),
    path('search/', views.search, name='search'),
    path('levels/', include('levels_app.urls')),

]