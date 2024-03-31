from django.forms import ModelForm, TextInput, FileInput

from levels_app.models import Level


class LevelUpForm(ModelForm):
    class Meta:
        model = Level
        fields = ['your_id', 'your_file']

        widgets = {
            'your_id': TextInput(attrs={
                'class': "form-control",
                'placeholder': '회원님의 아이디를 입력해주세요.'
            }),

            'age': FileInput(attrs={
                'class': "form-control",
                'placeholder': '등업에 필요한 자료를 첨부해주세요.'
            }),
        }