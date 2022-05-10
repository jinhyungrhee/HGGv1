from django.contrib.auth import authenticate, login
from django.http import request
from django.shortcuts import redirect, render
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, ListView, DetailView
from django.views.generic.list import MultipleObjectMixin
from .models import Product, Review
from .forms import RegisterForm, UserForm
from .models import Product, Review, Apply, Post
from .forms import RegisterForm
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Q
class ProductList(ListView):
    model = Product
    template_name = 'goods/goodsList.html'

class ProductCreate(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Product
    fields = '__all__'
    template_name = 'goods/goodsRegister.html'
    success_url = '../complete1/'

    def post(self, request, *args, **kwargs):
        self.object = None
        return super().post(request, *args, **kwargs)

class ReviewList(ListView):
    model = Review
    template_name = 'review/reviewList.html'

class ReviewCreate(CreateView):
    model = Review
    fields = '__all__'
    template_name = 'review/review-post.html'
    success_url = '../complete2/'

    def post(self, request, *args, **kwargs):
        self.object = None
        return super().post(request, *args, **kwargs)

class ReviewDetail(DetailView):
    model = Review # queryset = Product.objects.all()과 동일
    template_name = 'review/reviewDetail.html'
    context_object_name = "review"

    # pk 가져오기
    def get_context_data(self, **kwargs):
        #생성된 context는 Template으로 전달됨
        context = super().get_context_data(**kwargs)
        #context['prodcut_list'] = Product.objects.filter()
        return context

def signup(request):
    # 계정 생성
    if request.method == "POST":
        
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password2')
            user = authenticate(username=username, password=raw_password)
            login(request, user) #로그인
            return redirect('/')

    else:
        form = UserForm()
    return render(request, 'signup/signup.html', {'form': form})

class UserLoginView(LoginView):
    template_name = 'login/login.html'
    def form_invalid(self, form):
        messages.error(self.request, '로그인에 실패하였습니다.')
        return super().form_invalid(form)

class GoodsDetail(DetailView):
    model = Product # queryset = Product.objects.all()과 동일
    template_name = 'goods/goodsDetail.html'
    context_object_name = "product"

    # pk 가져오기
    def get_context_data(self, **kwargs):
        #생성된 context는 Template으로 전달됨
        context = super().get_context_data(**kwargs)
        #context['prodcut_list'] = Product.objects.filter()
        return context

class ApplyCreate(CreateView):
    model = Apply
    fields = '__all__'
    template_name = 'goods/purchase.html'
    success_url = '../complete3/'

    def post(self, request, *args, **kwargs):
        self.object = None
        return super().post(request, *args, **kwargs)

#공지사항 관련 API
def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'notice/notice-board.html', context={'posts':posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    return render(request, 'notice/notice-detail.html', context={'post':post })

def post_write(request):
    errors = []
    if request.method =='POST':
        user = User.objects.get(email=(request.session.get('user')))
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()
        image = request.FILES.get('image')

        if not title:
            errors.append("제목을 입력해주세요.")

        if not content:
            errors.append("내용을 입력해주세요.")

        if not errors:
            post = Post.objects.create(user=user, title=title, content=content, image=image)
            return redirect(reverse('post_detail', kwargs={'post_id':post.id}))

    return render(request, 'notice/notice-post.html', {'errors':errors})

#상품 검색 기능 API
def searchResult(request):
    products = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Product.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))
    
    return render(request, 'search/search.html', {'query':query, 'products':products})