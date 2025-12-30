from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import F,Q,Sum,Count
from magazine.models import Magazine, Magazine_code


def mview(request,mno):
    
    qs = Magazine.objects.get(mno=mno)
    
    qs_pre = Magazine.objects.filter(mdate__lt=qs.mdate).order_by('-mdate').first()
    qs_next = Magazine.objects.filter(mdate__gt=qs.mdate).order_by('mdate').first()
    
    context = {'mno':mno,'mz':qs,'pre':qs_pre,'next':qs_next}
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


