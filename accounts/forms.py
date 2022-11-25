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
        self.fields["college"].label = "학부대학(college)"
        self.fields["email"].widget.attrs = {
            "class": "form-control",
            "rows": 15,
        }
        self.fields["email"].label = "이메일(email)"

        self.fields["password"].widget.attrs = {
            "class": "form-control",
            "rows": 15,
        }
        self.fields["password"].label = "비밀번호(password)"
        self.fields["name"].widget.attrs = {
            "class": "form-control",
            "rows": 15,
        }
        self.fields["name"].label = "이름(name)"
        self.fields["studentID"].widget.attrs = {
            "class": "form-control",
            "rows": 15,
        }
        self.fields["studentID"].label = "학번(studentID)"
        self.fields["gpa"].widget.attrs = {
            "class": "form-control",
            "rows": 10,
            "step": 0.01,
        }
        self.fields["gpa"].label = "계열전공진입학점(gpa)"
        self.fields["gpa_all"].widget.attrs = {
            "class": "form-control",
            "rows": 10,
            "step": 0.01,
        }
        self.fields["gpa_all"].label = "융합전공진입학점(gpa_all)"
        self.fields["identifier_image"].widget.attrs = {
            "class": "form-control",
            "rows": 10,
        }
        self.fields["identifier_image"].label = "학교 인증 사진(필수X | identifier_image)"
        self.fields["major"].widget.attrs = {
            "class": "form-control",
            "rows": 10,
        }
        self.fields["major"].label = "지망학과(going major)"


class UserEditForm(forms.ModelForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'studentID',
                  'name', 'college', 'gpa', 'gpa_all', 'identifier_image', 'major')

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)

        self.fields["college"].widget.attrs = {
            "class": "form-control",
            "rows": 15,
        }
        self.fields["college"].label = "학부대학(college)"
        self.fields["email"].widget.attrs = {
            "class": "form-control",
            "rows": 15,
        }
        self.fields["email"].label = "이메일(email)"

        self.fields["name"].widget.attrs = {
            "class": "form-control",
            "rows": 15,
        }
        self.fields["name"].label = "이름(name)"
        self.fields["studentID"].widget.attrs = {
            "class": "form-control",
            "rows": 15,
        }
        self.fields["studentID"].label = "학번(studentID)"
        self.fields["gpa"].widget.attrs = {
            "class": "form-control",
            "rows": 10,
            "step": 0.01,
        }
        self.fields["gpa"].label = "계열전공진입학점(gpa)"
        self.fields["gpa_all"].widget.attrs = {
            "class": "form-control",
            "rows": 10,
            "step": 0.01,
        }
        self.fields["gpa_all"].label = "융합전공진입학점(gpa_all)"
        self.fields["identifier_image"].widget.attrs = {
            "class": "form-control",
            "rows": 10,
        }
        self.fields["identifier_image"].label = "학교 인증 사진(identifier_image)"
        self.fields["major"].widget.attrs = {
            "class": "form-control",
            "rows": 10,
        }
        self.fields["major"].label = "지망학과(going major)"


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
        self.fields["title"].label = "강의이름(title)"

        self.fields["lecture_type"].widget.attrs = {
            "class": "form-control",
            "rows": 10,
        }
        self.fields["lecture_type"].label = "강의유형(lecture type)"

        self.fields["point"].widget.attrs = {
            "class": "form-control",
            "rows": 10,
        }
        self.fields["point"].label = "단위수/시수(point)"

        self.fields["score"].widget.attrs = {
            "class": "form-control",
            "rows": 10,
        }
        self.fields["score"].label = "평점(score)"
