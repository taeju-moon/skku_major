from django.shortcuts import get_object_or_404, render, redirect
from snsapp.forms import PostForm, CommentForm
from snsapp.models import Post, Comment
from accounts.models import User
from django.core.paginator import Paginator

# https://ssungkang.tistory.com/entry/Django-11-Pagination-%EC%9D%84-%EC%95%8C%EC%95%84%EB%B3%B4%EC%9E%90
# pagination


def about(request):
    return render(request, "about.html")


def home(request):
    if (request.method == "GET" or request.POST["college"] == "ALL"):
        posts = Post.objects.all().order_by("-date")
        paginator = Paginator(posts, 10)
        page = request.GET.get("page")
        final_posts = paginator.get_page(page)
        return render(request, "home.html", {"posts": final_posts})
    else:
        posts = Post.objects.filter(
            college=request.POST["college"]).order_by("-date")
        paginator = Paginator(posts, 10)
        page = request.GET.get("page")
        final_posts = paginator.get_page(page)
        return render(request, "home.html", {"posts": final_posts})


def postcreate(request):
    if request.method == "POST" or request.method == "FILES":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            finished_form = form.save(commit=False)
        finished_form.writer = get_object_or_404(
            User, studentID=request.user.studentID)
        finished_form.save()
        return redirect("home")
    else:
        form = PostForm()
        return render(request, "post_form.html", {"form": form})


def postedit(request, post_id):
    if request.method == "GET":
        using = get_object_or_404(Post, pk=post_id)
        form = PostForm(instance=using)
        return render(request, "edit_post.html", {"form": form, "post_id": post_id})
    else:
        using = get_object_or_404(Post, pk=post_id)
        using.title = request.POST["title"]
        using.body = request.POST["body"]
        using.college = request.POST["college"]
        using.save()
        comment_form = CommentForm()
        return render(request, "detail.html", {"post": using, "comment_form": comment_form})


def post_delete(request, post_id):
    Post.objects.filter(id=post_id).delete()
    return redirect("home")


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comment_form = CommentForm()
    return render(request, "detail.html", {"post": post, "comment_form": comment_form})

# save comment


def create_comment(request, post_id):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Post, pk=post_id)
        finished_form.writer = get_object_or_404(
            User, studentID=request.user.studentID)
        finished_form.save()
    return redirect("detail", post_id)


def delete_comment(request, comment_id, post_id):
    Comment.objects.filter(id=comment_id).delete()
    return redirect("detail", post_id)
