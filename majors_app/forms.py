from django.forms import ModelForm

from majors_app.models import Majors


class MajorAddForm(ModelForm):
    class Meta:
        model = Majors
        fields = ['major_name', 'image']