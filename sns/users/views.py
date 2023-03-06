from django.shortcuts import render, redirect, get_object_or_404

from main.models import Blog
from django.contrib.auth.models import User

def mypage(request, id):
    user = get_object_or_404(User, pk=id)
    context = {
        'user':user,
        'blogs':Blog.objects.filter(writer=user),
        # 'followings' : 팔로잉 전체 불러오기,
        # 'followers' : 팔로워 전체 불러오기,
    }
    return render(request, 'users/mypage.html', context)

# follow 함수 작성
# follow 함수 정의(id값 받기):
#     user = 요청한 유저
#     followed_user = 파라미터로 받은 id에 해당하는 객체를 User 모델에서 가져온다
#     is_follower(Boolean) = 팔로우 한 사람들 리스트에 요청한 유저가 있는지 확인
#     있다면:
#         followed_user를 팔로잉 목록에서 지운다
#     아니라면:
#         followed_user를 팔로잉 목록에 추가한다
#     followed_user.id와 함께 'users:mypage'로 redirect한다.