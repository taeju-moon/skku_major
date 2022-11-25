from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import User

# enum: https://stackoverflow.com/questions/54802616/how-to-use-enums-as-a-choice-field-in-django-model


class College(models.TextChoices):
    HUMANITY = '인문과학계열', _('인문과학계열(HUMANITY)')
    SOCIETY = '사회과학계열', _('사회과학계열(SOCIETY)')
    SCIENCE = '자연과학계열', _('자연과학계열(SCIENCE)')
    ENGINNERING = '공학계열', _('공학계열(ENGINNERING)')
    FREE = '자유게시판', _('자유게시판(FREE)')

# 게시글 모델(익명게시판)


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey(
        User, on_delete=models.CASCADE, db_column="studentID", null=True)

    college = models.CharField(
        max_length=10,
        choices=College.choices,
        default=College.HUMANITY,
    )

    def __str__(self):
        return self.title

# 댓글 모델(익명게시판)


class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(
        Post, null=True, on_delete=models.CASCADE, db_column="post_id")
    writer = models.ForeignKey(
        User, on_delete=models.CASCADE, db_column="studentID", null=True)

    def __str__(self):
        return self.comment
