from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from levels_app.decorators import level_up_ownership_required
from levels_app.forms import LevelUpForm
from levels_app.models import Level





class LevelUpView(CreateView):
    model = Level
    context_object_name = 'target_level'
    form_class = LevelUpForm
    template_name = 'levels_app/create.html'

    def form_valid(self, form):
        temp_profile = form.save(commit=False)
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accounts_app:detail', kwargs={'pk': self.object.user.pk})



@method_decorator(level_up_ownership_required, 'get')
@method_decorator(level_up_ownership_required, 'post')
class LevelUpUpdateView(UpdateView):
    model = Level
    context_object_name = 'target_level'
    form_class = LevelUpForm
    template_name = 'levels_app/update.html'

    def get_success_url(self):
        return reverse('accounts_app:detail', kwargs={'pk': self.object.user.pk})
