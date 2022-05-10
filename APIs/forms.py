from django import forms
from django.forms import fields
from .models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product, Review

# 일단 사용 X
# 일단은 formView대신 CreateView 사용해서 상품입력 완성했음

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Product
        # 일단 'created_at'은 제외
        fields = ['name', 'price', 'description']

class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    nickname = forms.CharField(max_length=256, label="닉네임")
    kakaoId = forms.CharField(max_length=256, label="카카오톡 ID")

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username is not unique")
        return username
    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email", "nickname", "kakaoId"]
class RegisterForm(forms.Form):

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    name = forms.CharField(
        error_messages={'required':"상품명을 입력하세요."},
        max_length=32, label="상품명"
    )
    price = forms.IntegerField(
        error_messages={'required': "상품가격을 입력하세요."},
        label="가격"
    )
    description = forms.CharField(
        error_messages={'required': "상품설명을 입력하세요."},
        label="상품설명"
    )
    image = forms.ImageField(
        error_messages={'required': "이미지를 등록하세요."},
        label="이미지"
    )
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        price = cleaned_data.get('price')
        description = cleaned_data.get('description')
        image = cleaned_data.get('image')

        if not(name and price and description and image):
            self.add_error('name', '값이 없습니다.')
            self.add_error('price', '값이 없습니다.')
            self.add_error('description', '값이 없습니다.')
            self.add_error('image', '값이 없습니다.')
