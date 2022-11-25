from django.shortcuts import render, redirect
from accounts.models import User

humanity_major = ["유학동양학과", "국어국문학과", "영어영문학과", "프랑스어문학과",
                  "러시아어문학과", "중어중문학과", "독어독문학과", "한문학과", "사학과", "철학과", "문헌정보학과"]

society_major = ["행정학과", "정치외교학과", "미디어커뮤니케이션학과", "사회학과",
                 "사회복지학과", "심리학과", "소비자학과", "아동&청소년학과", "경제학과", "통계학과"]

science_major = ["생명과학과", "수학과", "물리학과",
                 "화학과", "식품생명공학과", "바이오메카트로닉스학과", "융합생명공학과"]

eng_major = ["화학공부/고분자시스템공학부", "신소재공학부",
             "기계공학부", "건설환경공학부", "시스템경영공학과", "나노공학과"]

sco = ["데이터사이언스융합전공", "인공지능융합전공", "컬처앤테크놀로지융합전공"]

majors = humanity_major+society_major+science_major+eng_major+sco


def is_in_users(user, users):
    for index, data in enumerate(users):
        if user.studentID == data.studentID:
            position = {"place": index+1, "people": len(users)}
            return position
    return None


def home(request):
    if not request.user.is_authenticated:
        return redirect("login")
    if request.method == "GET":
        return render(request, "score.html", {"majors": majors})
    else:
        standard = "-gpa"
        if request.POST["major"] in sco:
            standard = "-gpa_all"
        if request.POST["major"] == "all":
            return redirect("score")

        if request.POST["accepted"] == "True":
            users = list(User.objects.filter(
                major=request.POST["major"], accepted=True).order_by(standard))
            position = is_in_users(request.user, users)
            return render(request, "score.html", {"majors": majors, "users": users, "position": position})
        else:
            users = list(User.objects.filter(
                major=request.POST["major"]).order_by(standard))
            position = is_in_users(request.user, users)
            return render(request, "score.html", {"majors": majors, "users": users, "position": position})
