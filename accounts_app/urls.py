from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from accounts_app.views import AccountsCreateView, AccountsUpdateView, AccountsDeleteView, AccountsDetailView


app_name = "accounts_app"


urlpatterns = [

    path('login/', LoginView.as_view(template_name='accounts_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', AccountsCreateView.as_view(), name='create'),
    path('detail/<int:pk>', AccountsDetailView.as_view(), name='detail'),
    path('update/<int:pk>', AccountsUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountsDeleteView.as_view(), name='delete'),

]