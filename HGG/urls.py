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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # 분리 필요성 논의
    path('', include('Pages.urls')),
    # allauth
    # TODO : 뷰 접근 제어 코드 추가
    # 이메일 확인 필요 페이지
    path(
        'email-confirmation-required/',
        TemplateView.as_view(template_name="account/email_confirmation_required.html"),
        name="account_email_confirmation_required",
    ), 
    # 이메일 확인 완료 페이지
    path(
        'email-confirmation-done/',
        TemplateView.as_view(template_name="account/email_confirmation_done.html"),
        name="account_email_confirmation_done",
    ), 
    # 비밀번호 변경 -> 일단 필요X
    # 장고에서 단순 템플릿을 랜더링할 때 제네릭뷰(템플릿뷰) 사용! (뷰 자리에 템플릿 뷰 사용)
    # path('password/change/', # ** allauth에도 존재하지만 패턴 매칭 순서상 먼저 매칭되어 적용됨 **
    # CustomPasswordChangeView.as_view(), # 클래스 뷰를 쓸 때는 as_view() 사용
    # name="account_password_change",
    # ), 
    # 회원가입/로그인/로그아웃 페이지
    path('', include('allauth.urls')), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # url for media
