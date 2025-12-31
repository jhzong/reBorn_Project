from django.contrib import admin
<<<<<<< HEAD
from member.models import MyUser

# Register your models here.

admin.site.register(MyUser)
=======
from .models import MyUser # 사용자님의 모델 클래스명

admin.site.register(MyUser)
>>>>>>> 9e24702e16192b0a198b0ff9b6c1082391e46742
