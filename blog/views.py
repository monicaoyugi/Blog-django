from django.shortcuts import render

# Create your views here.
posts = [
    {
        "author": "Monica",
        "title": "Blog Post 1",
        "content": "First post",
        "date_posted": "May 07, 202",
    },
    {
        "author": "Kisinga",
        "title": "Blog Post 2",
        "content": "First post",
        "date_posted": "May 07, 202",
    },
]


def home(request):
    context = {"posts": posts}
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
