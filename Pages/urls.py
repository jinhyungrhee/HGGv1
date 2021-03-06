"""HGG URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import * # Pages.views.py
from django.contrib.auth import views
from APIs.views import ProductCreate, ProductList, ReviewCreate, ReviewList, GoodsDetail, ApplyCreate, posts_list, review_list, ReviewDetail, post_detail, searchResult, draw, myProduct, myProductDetail
# from APIs.views import ProductCreate, ProductList, ReviewCreate, ReviewList, GoodsDetail, ApplyCreate, signup, UserLoginView, posts_list, ReviewDetail, post_detail, searchResult

urlpatterns = [
    path('noticeBoard/', posts_list, name="noticeBoard"),
    # path('noticePost/', noticePost, name="noticePost"), # 일단 사용X
    #공지사항 디테일
    path('noticeDetail/<int:post_id>', post_detail, name="noticeDetail"),
    path('', index, name="index"),
    # 신청하기
    path('applyProduct/<int:purchase_id>', ApplyCreate.as_view(), name="purchase"),
    # 수정 : path('register/', register, name="register"),
    path('productRegister/', ProductCreate.as_view(), name='register'),
    # 상품리스트 보여주기
    path('productList/', ProductList.as_view(), name='productList'),
    path('writeReview/<int:purchase_id>', ReviewCreate.as_view(), name="writeReview"),
    # 리뷰리스트 보여주기
    path('reviewList/', ReviewList.as_view(), name='reviewList'),
    # path('reviewList/', review_list, name='reviewList'),
    # 상품등록 완료 페이지
    path('completeRegister/', registerComplete, name="registerComplete"),
    # 리뷰등록 완료 페이지
    path('completeReview/', reviewComplete, name="reviewComplete"),
    # 로그인 -> **수정필요**
    # path('login/', UserLoginView.as_view(), name="loginIndex"),
    # 로그아웃 -> **수정필요**
    path('account/logout/', views.LogoutView.as_view(), name='logout'),
    # 신청 완료 페이지
    path('completeApply/', applyComplete, name="applyComplete"),
    # path('userInformation/', userInformation, name="userInformation"), # 사용X
    # 회원가입 -> **수정필요**
    # path('signup/', signup, name="signup"),
    # 상품 상세보기
    path('productDetail/<int:pk>', GoodsDetail.as_view(), name="goodsDetail"),
    # path('reviewBoard/', reviewBoard, name="reviewBoard"), # 사용X
    # path('submitComplete/',submitComplete,name="submitComplete"), # 사용X
    # 리뷰 자세히
    path('reviewDetail/<int:pk>', ReviewDetail.as_view(), name="reviewDetail"),
    # 검색 기능
    path('searchProduct/', searchResult, name='search'),
    # 내 신청 물품보기 기능
    path('myProduct/', myProduct, name='myProduct'),
    path('myProductDetail/<int:pk>', myProductDetail.as_view(), name="myProductDetail"),
    # 시안제작 기능
    path('drawHufs/', drawHufs, name='drawHufs'),
    path('drawKhu/', drawKhu, name='drawKhu'),
]
