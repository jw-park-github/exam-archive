from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.views.generic import ListView
from subjects_app.models import Subjects


def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        s_names_list = Subjects.objects.filter(subject_name__contains=searched)
        return render(request, 'searched.html', {'searched': searched, 's_names_list': s_names_list})
    else:
        return render(request, 'searched.html', {})



class SubjectsListView(ListView):
    model = Subjects
    context_object_name = 'subjects_list'
    template_name = 'subjects_app/list.html'
    paginate_by = 20

    def get_queryset(self):
        return Subjects.objects.all().order_by('-pk')

def level_up(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'level_up.html', context)