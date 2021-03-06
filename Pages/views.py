from django.shortcuts import render, get_object_or_404

# Create your views here.
# def noticePost(request):
#     return render(request, 'notice/notice-post.html')

def index(request):
    return render(request, 'main/index.html')

# def purchase(request):
#     return render(request, 'goods/purchase.html')

# review 테스트중 -> 사용X
# def review(request):
#     return render(request, 'review/review-post.html')

# 상품등록완료
def registerComplete(request):
    return render(request, 'complete/register-complete.html')

# 리뷰등록완료
def reviewComplete(request):
    return render(request, 'complete/review-complete.html')

# def userInformation(request):
#     return render(request, 'login/input-user-information.html')

# def goodsDetail(request): # APIs.views.py의 GoodsDetail 클래스뷰와 중복!
#     return render(request, 'goods/goodsDetail.html')

# def reviewBoard(request):
#     return render(request, 'review/review-board.html')

# def submitComplete(request):
#     return render(request, 'complete/submit-complete.html')

# 신청 완료 페이지
def applyComplete(request):
    return render(request, 'complete/apply-complete.html')

# 시안 제작 페이지
def draw(request):
    return render(request, 'drawing/draw-board.html')

def drawHufs(request):
    return render(request, 'drawing/draw-board-hufs.html')

def drawKhu(request):
    return render(request, 'drawing/draw-board-khu.html')