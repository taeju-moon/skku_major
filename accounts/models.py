from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import MinValueValidator, MaxValueValidator


class College(models.TextChoices):
    HUMANITY = '인문과학계열', _('인문과학계열(HUMANITY)')
    SOCIETY = '사회과학계열', _('사회과학계열(SOCIETY)')
    SCIENCE = '자연과학계열', _('자연과학계열(SCIENCE)')
    ENGINNERING = '공학계열', _('공학계열(ENGINNERING)')


class Major(models.TextChoices):
    EASTERN = '유학동양학과', _('유학동양학과')
    KOREAN = '국어국문학과', _('국어국문학과')
    ENGLISH = '영어영문학과', _('영어영문학과')
    FRENCH = '프랑스어문학과', _('프랑스어문학과')
    RUSSIAN = '러시아어문학과', _('러시아어문학과')
    CHINA = '중어중문학과', _('중어중문학과')
    GERMANY = '독어독문학과', _('독어독문학과')
    CHINESECHARACTER = '한문학과', _('한문학과')
    HISTORY = '사학과', _('사학과')
    PHILOSOPHY = '철학과', _('철학과')
    INFO = '문헌정보학과', _('문헌정보학과')
    PUBADMIN = '행정학과', _('행정학과')
    WIZ = '정치외교학과', _('정치외교학과')
    COMM = '미디어커뮤니케이션학과', _('미디어커뮤니케이션학과')
    SOCIO = '사회학과', _('사회학과')
    WELFARE = '사회복지학과', _('사회복지학과')
    HOME = '심리학과', _('심리학과')
    EXPENSE = '소비자학과', _('소비자학과')
    CHILD = '아동&청소년학과', _('아동&청소년학과')
    ECO = '경제학과', _('경제학과')
    STATIC = '통계학과', _('통계학과')
    BIO = '생명과학과', _('생명과학과')
    MATH = '수학과', _('수학과')
    PHYSICS = '물리학과', _('물리학과')
    CHEMIST = '화학과', _('화학과')
    EAT = '식품생명공학과', _('식품생명공학과')
    BIOM = '바이오메카트로닉스학과', _('바이오메카트로닉스학과')
    SHB = '융합생명공학과', _('융합생명공학과')
    ENC = '화학공부/고분자시스템공학부', _('화학공부/고분자시스템공학부')
    WEB = '신소재공학부', _('신소재공학부')
    MECH = '기계공학부', _('기계공학부')
    BUILD = '건설환경공학부', _('건설환경공학부')
    SYSTEM = '시스템경영공학과', _('시스템경영공학과')
    NANO = '나노공학과', _('나노공학과')
    DSC = '데이터사이언스융합전공', _('데이터사이언스융합전공')
    AAI = '인공지능융합전공', _('인공지능융합전공')
    CNT = '컬처앤테크놀로지융합전공', _('컬처앤테크놀로지융합전공')


humanity_major = ["유학동양학과", "국어국문학과", "영어영문학과", "프랑스어문학과",
                  "러시아어문학과", "중어중문학과", "독어독문학과", "한문학과", "사학과", "철학과", "문헌정보학과"]

society_major = ["행정학과", "정치외교학과", "미디어커뮤니케이션학과", "사회학과",
                 "사회복지학과", "심리학과", "소비자학과", "아동&청소년학과", "경제학과", "통계학과"]

science_major = ["생명과학과", "수학과", "물리학과",
                 "화학과", "식품생명공학과", "바이오메카트로닉스학과", "융합생명공학과"]

eng_major = ["화학공부/고분자시스템공학부", "신소재공학부",
             "기계공학부", "건설환경공학부", "시스템경영공학과", "나노공학과"]

sco = ["데이터사이언스융합전공", "인공지능융합전공", "컬처앤테크놀로지융합전공"]


class UserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, name, studentID, email, college, gpa, gpa_all, identifier_image, major, password=None):

        def validate_major(college, major):
            if major in sco:
                return True
            else:
                if college == "인문과학계열":
                    return major in humanity_major
                elif college == "사회과학계열":
                    return major in society_major
                elif college == "자연과학계열":
                    return major in science_major
                else:
                    return major in eng_major

        if not email:
            raise ValueError('must have user email')
        if not validate_major(college, major):
            raise ValueError("학과 정보가 계열에 상응하지 않습니다.")
        user = self.model(
            name=name,
            studentID=studentID,
            email=email,
            college=college,
            accepted=False,
            gpa=gpa,
            gpa_all=gpa_all,
            identifier_image=identifier_image,
            major=major,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, studentID, email, college, password):

        user = self.create_user(
            name=name,
            studentID=studentID,
            email=email,
            college=college,
            password=password,
            gpa=0.0,
            gpa_all=0.0,
            identifier_image=None,
            major="데이터사이언스융합전공"
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    objects = UserManager()

    name = models.CharField(
        max_length=255,
    )
    studentID = models.CharField(max_length=255, unique=True, primary_key=True)
    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    college = models.CharField(
        max_length=10,
        choices=College.choices,
    )

    accepted = models.BooleanField(default=False)

    gpa = models.FloatField(default=0.0, validators=[
                            MinValueValidator(0.0), MaxValueValidator(4.5)])
    gpa_all = models.FloatField(default=0.0, validators=[
                                MinValueValidator(0.0), MaxValueValidator(4.5)])
    identifier_image = models.ImageField(default=None, blank=True)
    major = models.CharField(
        max_length=200, choices=Major.choices, default=Major.DSC)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'studentID', 'college']


class LectureType(models.TextChoices):
    COMMUNICATE = '의사소통', _('의사소통(COMMUNICATE)')
    CREATIVE = '창의', _('창의(CREATIVE)')
    GLOBAL = '글로벌', _('글로벌(GLOBAL)')
    BSM = '기초인문사회/BSM', _('기초인문사회/BSM')
    LEADERSHIP = '성균인성/리더쉽(LEADERSHIP)', _('성균인성/리더쉽(LEADERSHIP)')
    BOOK = '고전명저', _('고전명저(BOOK)')
    DS = 'DS기반', _('DS기반(DS)')
    BALANCE = '핵심균형', _('핵심균형(BALANCE)')
    MAJOR_ = '전공일반/전공핵심', _('전공일반/전공핵심(MAJOR)')
    ETC = '일반선택', _('일반선택(ETC)')


class Score(models.TextChoices):
    AP = 'A+', _('A+')
    A = 'A', _('A')
    BP = 'B+', _('B+')
    B = 'B', _('B')
    CP = 'C+', _('C+')
    C = 'C', _('C')
    DP = 'D+', _('D+')
    D = 'D', _('D')
    F = 'F', _('F')
    P = 'P', _('P')


class Lecture(models.Model):
    title = models.CharField(max_length=200)
    lecture_type = models.CharField(
        max_length=200, choices=LectureType.choices, default=LectureType.ETC)
    point = models.IntegerField(default=1)
    score = models.CharField(
        max_length=200, choices=Score.choices, default=Score.AP)
    writer = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE, db_column="studentID")

    REQUIRED_FIELDS = ['title', 'lecture_type', 'point', 'score']

    def __str__(self):
        return self.title
