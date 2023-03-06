from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog, User

from django.views.decorators.http import require_POST
# 2-2 response를 변환하는 가장 가본 함수, html 파일, 이미지 등 다양한 응답
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# 2-3 딕셔너리를 json 형식으로 바꾸기 위해
import json

# Create your views here.
def showmain(request):
    blogs = Blog.objects.all()
    return render(request, 'main/main.html', {'blogs':blogs})

def showdetail(request, id):
    blog = get_object_or_404(Blog, pk=id)
    return render(request, 'main/detail.html', {'blog':blog})

def shownew(request):
    return render(request, 'main/new.html')

def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.writer = request.user
    new_blog.pub_date = timezone.now()
    new_blog.body = request.POST['body']
    new_blog.save()
    return redirect('main:showdetail', new_blog.id)

def showupdate(request, id):
    update_blog = Blog.objects.get(id=id)
    return render(request, 'main/update.html', {'blog':update_blog})

def edit(request, id):
    update_blog = Blog.objects.get(id=id)
    update_blog.title = request.POST['title']
    update_blog.writer = request.user
    update_blog.pub_date = timezone.now()
    update_blog.body = request.POST['body']
    update_blog.save()
    return redirect('main:showdetail', update_blog.id)

def delete(request, id):
    delete_blog = Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect('main:showmain')

# likes 함수 작성
# likes 함수 정의(블로그 id 값 받기):
#     blog = 블로그 id에 맞는 게시물을 Blog로부터 가져오기
#     만약 좋아요를 누른 사람 중 자신이 있다면:
#         좋아요를 누른 사람 리스트에서 자신을 없애고
#         좋아요 개수에서 1을 뺴고
#         저장한다
#     아니라면:
#         좋아요를 누른 사람 리스트에 자신을 추가하고
#         좋아요 개수에서 1을 더하고
#         저장한다
#     블로그 id와 함께 'main:showdetail'로 redirect한다.
