from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MyUser # 우리가 만든 회원 창고(모델)를 가져온다
from django.contrib.auth.hashers import make_password # 비밀번호를 암호화해주는 도구

# 로그인 페이지
def login(request):
    if request.method == 'POST':
        # 입력된 데이터값을
        user_id = request.POST.get('id')
        user_pw = request.POST.get('pw')
        # 콘솔창에 띄운다.
        print(f"아이디 : {user_id}")
        print(f"비밀번호 : {user_pw}")
        
        
        
        return redirect('/')
    else:
        return render(request,'member/login.html')
    


# 회원가입 페이지
def join(request):
    return render(request,'member/join.html')

# 회원가입 페이지-1
def join1(request):
    return render(request,'member/join1.html')

# 회원가입 페이지-2
def join2(request):
    if request.method == "GET":
        return render(request,'member/join2.html')
    elif request.method == "POST":
        # HTML의 name="mem_id" 등으로 적었던 데이터들을 가져옵니다.
        mid = request.POST.get('mem_id')
        mpw = request.POST.get('mem_pw')
        mnm = request.POST.get('mem_nm')
        nnm = request.POST.get('nick_nm')
        eml = request.POST.get('email')
        phn = request.POST.get('phone_number')
        context = {}
        return render(request,'member/join3.html', context)


# 회원가입 페이지-3
def join3(request):
    if request.method == "GET":
        return render(request,'member/join3.html')
    elif request.method == "POST":
        # HTML의 name="mem_id" 등으로 적었던 데이터들을 가져옵니다.
        mid = request.POST.get('mem_id')
        mpw = request.POST.get('mem_pw')
        mnm = request.POST.get('mem_nm')
        nnm = request.POST.get('nick_nm')
        eml = request.POST.get('email')
        phn = request.POST.get('phone_number')
        
        # db저장 부분
        # 데이터를 DB에 저장 (비밀번호는 꼭 암호화해서 저장!)
        user = MyUser(
            mem_id = mid,
            mem_pw = make_password(mpw), # 비밀번호를 숫자가 아닌 외계어로 바꿔서 저장
            mem_nm = mnm,
            nick_nm = nnm,
            email = eml,
            phone_number = phn
        )
        user.save() # 실제로 DB에 저장하는 순간!
        
        # 저장이 끝났으면 03단계(완료 페이지)로 보냅니다.
        return redirect('member:join3') 
        # return redirect('member:join2') # 잘못 들어오면 다시 뒤로

def join_save(request):
    if request.method == "POST":
        return redirect('/?result=1') # 잘못 들어오면 다시 뒤로



