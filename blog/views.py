from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all().order_by('-pk')      #이 파일에서 데이터베이스에 쿼리를 날려 원하는 레코드 (pk 값의 역순으로 정렬되어) 가져오는 코드.


    return render(
        request,
        'blog/index.html',
        {
            'posts': posts,
        }
    )

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)      # Post.objects.get(): 괄호 안의 조건을 만족하는 Post 레코드를 가져오라

    return render(
        request,
        'blog/single_post_page.html',
        {
            'post': post,
        }
    )