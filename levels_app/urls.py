from django.urls import path

from levels_app.views import LevelUpView, LevelUpUpdateView

app_name = 'levels_app'

urlpatterns = [
    path('create/', LevelUpView.as_view(), name='create'),
    path('update/<int:pk>', LevelUpUpdateView.as_view(), name='update'),

]