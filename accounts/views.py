from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from accounts.models import User, Lecture
from accounts.forms import UserForm, UserEditForm, LectureForm


def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST['password']
        user = auth.authenticate(request, email=email, password=password)
        if user:
            auth.login(request, user)
            return redirect("home")
        else:
            return render(request, "bad.html")
    else:
        return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect("home")


def register(request):
    if request.method == "GET":
        form = UserForm()
        return render(request, "register.html", {"form": form})
    elif request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(
                request.POST["name"], request.POST["studentID"], request.POST["email"], request.POST["college"],
                request.POST["gpa"], request.POST["gpa_all"], request.POST["identifier_image"], request.POST["major"], request.POST["password"])
            auth.login(request, new_user)
            return redirect("home")
        else:
            return redirect("register")


def mypage(request):
    if request.user.is_authenticated:
        lectures = Lecture.objects.filter(writer=request.user.studentID)
        return render(request, "mypage.html", {"lectures": lectures})
    else:
        return redirect("login")


def editmypage(request):
    if request.method == "GET":
        my_record = User.objects.get(studentID=request.user.studentID)
        form = UserEditForm(instance=my_record)
        return render(request, "editmypage.html", {"form": form})
    else:
        user = request.user
        user.name = request.POST["name"]
        user.studentID = request.POST["studentID"]
        user.email = request.POST["email"]
        user.college = request.POST["college"]
        user.gpa = request.POST["gpa"]
        user.gpa_all = request.POST["gpa_all"]
        user.identifier_image = request.POST["identifier_image"]
        user.major = request.POST["major"]
        user.save()
        return redirect("mypage")


def add_lecture(request):
    if request.method == "GET":
        form = LectureForm()
        return render(request, "addlecture.html", {"form": form})
    else:
        filled_form = LectureForm(request.POST)
        if filled_form.is_valid():
            finished_form = filled_form.save(commit=False)
            finished_form.writer = get_object_or_404(
                User, pk=request.user.studentID)
            finished_form.save()
        lectures = Lecture.objects.filter(writer=request.user.studentID)
        return render(request, "mypage.html", {"lectures": lectures})


def edit_lecture(request, lecture_id):
    if request.method == "GET":
        using = get_object_or_404(Lecture, pk=lecture_id)
        form = LectureForm(instance=using)
        return render(request, "editlecture.html", {"form": form, "lecture_id": lecture_id})
    else:
        using = get_object_or_404(Lecture, pk=lecture_id)
        using.title = request.POST["title"]
        using.lecture_type = request.POST["lecture_type"]
        using.point = request.POST["point"]
        using.score = request.POST["score"]
        using.save()
        return redirect("mypage")


def delete_lecture(request, lecture_id):
    Lecture.objects.filter(id=lecture_id).delete()
    return redirect("mypage")


def get_score(score):
    if score == "A+":
        return 4.5
    elif score == "A":
        return 4.0
    elif score == "B+":
        return 3.5
    elif score == "B":
        return 3.0
    elif score == "C+":
        return 2.5
    elif score == "C":
        return 2.0
    elif score == "D+":
        return 1.5
    elif score == "D":
        return 1.0
    else:
        return 0


using_lecture_types = ["의사소통", "창의", "글로벌", "기초인문사회/BSM", "고전명저", "DS기반"]


def get_gpa(lectures):
    all_points = 0
    all_scores = 0
    for lecture in lectures:
        all_points += lecture.point
        all_scores += get_score(lecture.score) * lecture.point
    if (all_points == 0 or all_scores == 0):
        return 0
    else:
        return round(all_scores/all_points, 2)


def apply_score(request):
    lectures = list(Lecture.objects.filter(writer=request.user.studentID))
    lectures = list(filter(lambda lecture: lecture.score != "P", lectures))
    lectures_gpa = list(filter(
        lambda lecture: lecture.lecture_type in using_lecture_types, lectures))
    lectures_all = lectures
    gpa = get_gpa(lectures_gpa)
    gpa_all = get_gpa(lectures_all)
    user = request.user
    user.gpa = gpa
    user.gpa_all = gpa_all
    user.save()

    return redirect("mypage")
