from django.shortcuts import render, HttpResponse
from .models import Post


def post_list(request):
    """
    Read(R)
    포스트들을 불러와서 리스트 형태로 보여준다.
    """

    posts = Post.objects.all()
    ctx = {'posts': posts}
    return render(request, template_name='posts/list.html', context=ctx)
# Create your views here.
