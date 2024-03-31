from django.urls import reverse
from django.views.generic import DetailView, ListView, CreateView
from django.views.generic.list import MultipleObjectMixin
from majors_app.forms import MajorAddForm
from majors_app.models import Majors
from subjects_app.models import Subjects



class MajorsListView(ListView):
    model = Majors
    context_object_name = 'majors_list'
    template_name = 'majors_app/list.html'



class MajorsCreateView(CreateView):
    model = Majors
    form_class = MajorAddForm
    template_name = 'majors_app/create.html'

    def get_success_url(self):
        return reverse('majors_app:detail', kwargs={'pk': self.object.pk})


class MajorsDetailView(DetailView, MultipleObjectMixin):
    model = Majors
    context_object_name = 'target_major'
    template_name = 'majors_app/detail.html'

    paginate_by = 25

    def get_context_data(self, **kwargs):
        object_list = Subjects.objects.filter(major=self.get_object())
        return super(MajorsDetailView, self).get_context_data(object_list=object_list,  **kwargs)





