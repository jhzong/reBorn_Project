from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import F,Q,Sum,Count
<<<<<<< HEAD
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from magazine.models import Magazine, MagazineCode
from member.models import MyUser

import json
import urllib.request


def mnaver(request):
    
    client_id = "j7KaOMGirpd_EoxbjKDB"
    client_secret = "98WTnc2agN"
    encText = urllib.parse.quote("음식점매거진")
    url = "https://openapi.naver.com/v1/search/blog?query=" + encText # JSON 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)
        
    dData = json.loads(response_body)
    nlist = dData['items']
        
    context = {'nlist':nlist}
    return render(request,'magazine/mnaver.html', context)

def mlike(request):
    
    if request.method == 'POST':
        
        mno = request.POST.get('mno')
        qs_magazine = Magazine.objects.get(mno=mno)
        
        id = request.session['session_id']
        qs_myuser = MyUser.objects.get(mem_id=id)
        
        if qs_magazine.like.filter(pk=qs_myuser.mem_id).exists():
            qs_magazine.like.remove(qs_myuser)
            like_chk = 0
        else:
            qs_magazine.like.add(qs_myuser)
            like_chk = 1
        
        like_count = qs_magazine.like.count()
    
    context = {'result':'성공','like_chk':like_chk,'like_count':like_count}
    return JsonResponse(context)
=======
from magazine.models import Magazine, Magazine_code
>>>>>>> 9e24702e16192b0a198b0ff9b6c1082391e46742


def mview(request,mno):
    
    qs = Magazine.objects.get(mno=mno)
    
    qs_pre = Magazine.objects.filter(mdate__lt=qs.mdate).order_by('-mdate').first()
    qs_next = Magazine.objects.filter(mdate__gt=qs.mdate).order_by('mdate').first()
    
    context = {'mz':qs,'pre':qs_pre,'next':qs_next}
    return render(request,'magazine/mview.html',context)


def mlist(request):

    category = request.GET.get('category','')
    search = request.GET.get('search','')
    # print('category : ',category,'search : ',search)
    
    # 매거진 코드 정보
    qs_code = Magazine_code.objects.all()

    # 매거진 리스트
    if not category: # 공란 처리
        
        if not search: # 공란 처리
            qs = Magazine.objects.all().order_by('-mdate')
        else:
            qs = Magazine.objects.filter(Q(mtitle__contains=search)|Q(mcontent__contains=search))

    else:
        qs_category = Magazine_code.objects.get(mtype=category)
        qs = Magazine.objects.filter(magazine_code=qs_category).order_by('-mdate')

    # 패이징
    page = int(request.GET.get('page',1))
    paginator = Paginator(qs,20)
    qs_list = paginator.get_page(page)
    
    # 남은 화면 출력
    if paginator.count < 5:
        etc = 4 - paginator.count
    else:
        etc = 4 - (paginator.count % 4)
        
    context = {'qs_code':qs_code,'list':qs_list,'page':page,'etc_count':etc,'category':category,'search':search}
    return render(request,'magazine/mlist.html',context)


