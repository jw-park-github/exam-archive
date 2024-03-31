from django.contrib import admin
from import_export.widgets import ForeignKeyWidget

from majors_app.models import Majors
from .models import Subjects
from import_export import resources, fields
from import_export.admin import ImportExportMixin


class SubjectsInfoResource(resources.ModelResource):
    major = fields.Field(column_name='major', attribute='major',
    widget = ForeignKeyWidget(Majors, 'major_name'))


    class Meta:
        model = Subjects
        import_id_fields = ('major',)
        fields = ('major', 'year', 'semester', 'prof_name', 'subject_name', 'midterm', 'final_exam')
        exclude = ('midterm', 'final_exam','id')


class SubjectsAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = SubjectsInfoResource
    list_display = ['major', 'year', 'semester', 'prof_name', 'subject_name', 'midterm', 'final_exam']
    search_fields = ['major']


admin.site.register(Subjects, SubjectsAdmin)