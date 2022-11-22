from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from accounts.models import Lecture

User = get_user_model()


class UserForm(forms.ModelForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'studentID', 'password',
                  'name', 'college', 'gpa', 'gpa_all', 'identifier_image', 'major')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        self.fields["college"].widget.attrs = {
            "class": "form-control",
            "rows": 15,
        }
        self.fields["email"].widget.attrs = {
            "class": "form-control",
            "rows": 15,
        }

        self.fields["password"].widget.attrs = {
            "class": "form-control",
            "rows": 15,
        }
        self.fields["name"].widget.attrs = {
            "class": "form-control",
            "rows": 15,
        }
        self.fields["studentID"].widget.attrs = {
            "class": "form-control",
            "rows": 15,
        }
        self.fields["gpa"].widget.attrs = {
            "class": "form-control",
            "rows": 10,
            "step": 0.1,
        }
        self.fields["gpa_all"].widget.attrs = {
            "class": "form-control",
            "rows": 10,
            "step": 0.1,
        }
        self.fields["identifier_image"].widget.attrs = {
            "class": "form-control",
            "rows": 10,
        }


class UserEditForm(forms.ModelForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'studentID', 'password',
                  'name', 'college', 'gpa', 'gpa_all', 'identifier_image', 'major')

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)

        self.fields["college"].widget.attrs = {
            "class": "form-control",
            "rows": 15,
        }
        self.fields["email"].widget.attrs = {
            "class": "form-control",
            "rows": 15,
        }

        # hide password input
        self.fields["password"].widget = forms.HiddenInput()

        self.fields["name"].widget.attrs = {
            "class": "form-control",
            "rows": 15,
        }
        self.fields["studentID"].widget.attrs = {
            "class": "form-control",
            "rows": 15,
        }
        self.fields["gpa"].widget.attrs = {
            "class": "form-control",
            "rows": 10,
            "step": 0.1,
        }
        self.fields["gpa_all"].widget.attrs = {
            "class": "form-control",
            "rows": 10,
            "step": 0.1,
        }
        self.fields["identifier_image"].widget.attrs = {
            "class": "form-control",
            "rows": 10,
        }
        self.fields["major"].widget.attrs = {
            "class": "form-control",
            "rows": 10,
        }


class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['title', 'lecture_type', 'point', 'score']

    def __init__(self, *args, **kwargs):
        super(LectureForm, self).__init__(*args, **kwargs)

        self.fields["title"].widget.attrs = {
            "class": "form-control",
            "rows": 10,
        }

        self.fields["lecture_type"].widget.attrs = {
            "class": "form-control",
            "rows": 10,
        }

        self.fields["point"].widget.attrs = {
            "class": "form-control",
            "rows": 10,
        }

        self.fields["score"].widget.attrs = {
            "class": "form-control",
            "rows": 10,
        }
