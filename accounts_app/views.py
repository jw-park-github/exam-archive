from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DeleteView, UpdateView, DetailView, CreateView


from accounts_app.decorators import account_ownership_required
from accounts_app.forms import AccountsUpdateForm


has_ownership = [account_ownership_required, login_required]



class AccountsCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'accounts_app/create.html'

    def form_valid(self, form):
        """If the form is valid, save the associated model and log the user in."""
        user = form.save()
        login(self.request, user)

        return redirect(self.success_url)


class AccountsDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accounts_app/detail.html'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountsUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountsUpdateForm
    success_url = reverse_lazy('home')
    template_name = 'accounts_app/update.html'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountsDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accounts_app:login')
    template_name = 'accounts_app/delete.html'




