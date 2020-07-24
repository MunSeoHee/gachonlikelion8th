from django import forms


class PostForm(forms.Form):  # django의 폼을 상속
    title = forms.CharField(label='제목', max_length=200)
    content = forms.CharField(label="내용", widget=forms.Textarea)

-------------------------------------------------------------------------------------------
## Model Form 사용해보기

# from django import forms
from django.forms import ModelForm
from second.models import Post

from django.utils.translation import gettext_lazt as _


class PostForm(ModelForm):
    class Meta:
        model = Post  # 어떤 모델 클래스를 사용할 것인지
        fields = ['title', 'content']  # 입력받을 필드들
        labels = {
            'title': _('제목'),
            'content': _('내용'),
        }
        help_texts = {
            'title': _('제목을 입력해주세요.'),
            'content': _('내용을 입력해주세요.'),
        }
        error_messages = {
            'name': {
                'max_length': _("제목이 너무 깁니다. 30자 이하로 해주세요."),
            },
        }