from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from .validators import validate_no_special_characters, validate_hufs_email
# Create your models here.
# User 테이블 정의
class User(AbstractUser):

    UNIV_CHOICES = {
        ('한국외대', '한국외대'),
        ('경희대', '경희대')
    }

    email = models.EmailField(
        max_length=50,
        unique=True,
        validators=[validate_hufs_email],
        error_messages={'unique':'학교 이메일이 아닙니다.'},
        verbose_name="이메일"
    )
    nickname = models.CharField(
        max_length=15, 
        unique=True,
        null=True,
        validators=[validate_no_special_characters],
        error_messages={'unique' : '이미 사용중인 닉네임입니다.'},
        verbose_name="닉네임"
    )
    univ = models.CharField(max_length=10, choices=UNIV_CHOICES ,verbose_name='소속대학')
    # kakaoId = models.CharField(max_length=50, verbose_name="카카오톡 ID")

    def __str__(self):
        return self.username

# Product 테이블 정의
class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name='상품명')
    quantity = models.IntegerField(verbose_name='모집인원')
    due_date = models.DateTimeField(verbose_name='모집기간')
    price = models.IntegerField(verbose_name='상품가격')
    description = models.TextField(verbose_name='상품설명')
    image = models.ImageField(upload_to="product/", blank=True, null=True) # 여러개 등록 가능?
    tag = models.CharField(max_length=20, verbose_name='태그')
    kakao_link = models.TextField(verbose_name='오픈카톡')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'products_product'
        verbose_name = '상품'
        verbose_name_plural = '상품'

# Review 테이블 정의
class Review(models.Model):

    SATIS_CHOICES = {
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    }

    title = models.CharField(max_length=256, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    image = models.ImageField(upload_to="review/", blank=True, null=True)
    category = models.CharField(max_length=20, verbose_name='카테고리')
    store = models.CharField(max_length=20, verbose_name='업체')
    delivery = models.IntegerField(verbose_name='배송기간')
    price = models.IntegerField(verbose_name='가격')
    satisfaction = models.CharField(max_length=10, choices=SATIS_CHOICES, verbose_name='만족도')
    # 작성자 정보 추가 필요
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'review'
        verbose_name = '리뷰'
        verbose_name_plural = '리뷰'

# Apply 테이블 정의
class Apply(models.Model):

    SIZE_CHOICES = {
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large')
    }

    COLOR_CHOICES = {
        ('red', 'Red'),
        ('beige', 'Beige'),
        ('purple', 'Purple')
    }

    RECEIVE_CHOICES = {
        ('택배수령', '택배수령'),
        ('대면수령', '대면수령')
    }

    username = models.CharField(max_length=20, verbose_name='성명')
    quantity = models.IntegerField(verbose_name='수량')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES, verbose_name='사이즈', null='True')
    receive = models.CharField(max_length=10, choices=RECEIVE_CHOICES ,verbose_name='수령방법')
    address = models.CharField(max_length=50, verbose_name='주소', blank='True', null='True')
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, verbose_name='색상', null='True')
    req = models.TextField(verbose_name='요청사항', blank='True', null='True')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='신청날짜')

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'apply'
        verbose_name = '신청'
        verbose_name_plural = '신청'

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='작성자')
    title = models.CharField(max_length=255, verbose_name='공지제목',blank=False)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'post'
        verbose_name = '공지글'
        verbose_name_plural = '공지글'