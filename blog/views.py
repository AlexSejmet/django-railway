from django.shortcuts import render

# Create your views here.


def render_blog(request):
    return render(request, 'blog.html')