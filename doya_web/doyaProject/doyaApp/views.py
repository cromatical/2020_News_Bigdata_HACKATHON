from django.shortcuts import render, redirect

from .models import Profile
from django.contrib.auth.models import User
from django.contrib import auth


import os
import pandas as pd
import numpy as np

# Create your views here.

# data_path = r'\doyaProject\doyaApp\data'
# major_fold = os.listdir(data_path) 


def home(request):
                   
    # print(major_fold)
    
    return render(request, 'home.html')

def news_list(request):

    return render(request, 'list.html')


def login(request):
    
    if request.method == 'POST':
        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']
        user = auth.authenticate(request, username=user_id, password=user_pw)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error' : 'username or password is incorrect'})

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')

major_lst = ['간호', '건축', '경영', '공예', '관광', '광고', '교육', '교통&운송', '기계&금속',
    '농림&수산', '도시&토목', '디자인', '미술', '법', '뷰티아트', '사진&만화', '사회과학',
    '산업공학', '생명과학', '서비스', '소재&재료', '수의학', '식품', '약학', '언론', '언어&문학', '에너지', '연극&영화',
    '영상&예술', '유아교육', '음악', '응용소프트웨어', '의류', '인문과학', '자연과학', '전기&전자',
    '전산학&컴퓨터', '정보&통신', '조선', '체육', '초등교육', '치료&보건', '특수교육', '화공']

def signup(request):
    if request.method == 'POST':
        if request.POST['user_pw'] == request.POST['user_pw_check']:
            user = User.objects.create_user(
                username=request.POST['user_id'],
                password=request.POST['user_pw'],
                email=request.POST['user_email']
            )
            user_name = request.POST['user_name']
            user_phone_num = request.POST['user_phone_num']
            user_major = request.POST['major_lst']

            profile = Profile(user=user,
                            user_name=user_name,
                            user_phone_num=user_phone_num,
                            user_major=user_major)
            profile.save()
            auth.login(request, user)
            return redirect('login')
        return render(request, 'signup.html')

    context = {
        'major_lst' : major_lst
    }
    return render(request, 'signup.html', context)

            


def mypage(request):
    return render(request, 'mypage.html')

def list(request):
    return render(request, 'news_list.html')

def scrapbook(request):
    return render(request, 'scrapbook.html')

def scrapB1(request):
    return render(request, 'scrapB1.html')
