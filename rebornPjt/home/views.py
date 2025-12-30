from django.shortcuts import render
from restaurants.models import Restaurant

# Create your views here.
def index(request):
    return render(request, 'index.html')

def filPop(request):
    # 필터에 저장된 값들(블루리본에도 안 되어 있는걸로 보여서 X)
    context = {"req": request.GET}
    # 지역, 음식타입 테이블에 있는걸로 가져와서 팝업에 체크박스 생성
    # Restaurant_list = Restaurant.objects.all()
    return render(request, 'filPop.html', context)