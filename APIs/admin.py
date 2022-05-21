from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from APIs.models import Product, Review, Apply, Post, User

# Register your models here.
# User테이블 등록
admin.site.register(User, UserAdmin)
UserAdmin.fieldsets += (("custom fields", {"fields": ("nickname", "kakaoId", )}),)

@admin.register(Product) # 데코레이터 - register함수 대신 사용
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'image', 'created_at')
#admin.site.register(Product, ProductAdmin)

# Review 테이블 등록 - author 추가
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'image', 'category', 'store', 'delivery', 'price', 'satisfaction', 'author' ,'created_at')

# Apply 테이블 등록
@admin.register(Apply)
class ApplyAdmin(admin.ModelAdmin):
    list_display = ('username', 'quantity', 'size', 'receive', 'address', 'color', 'req', 'created_at')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'content', 'image', 'created_at', 'modified_at')