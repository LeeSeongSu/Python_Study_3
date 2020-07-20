# Python_Study_3
멋쟁이사자처럼(DB - Model/Admin 장고 공부)

## MTV패턴
- Model : 데이터 베이스를 담당. 데이터베이스에 어떤 정보를 받을지 정의하는 곳
- View : 데이터가 어떤 상황에서 어떤 식으로 처리되는 지에 대한 함수를 모아 놓은 곳
- Templates : Model에 있는 데이터를 사용자에게 어떻게 보여줄지 정하는 곳

## python manage.py makemigrations
- models.py에서 우리가 짠 python코드를 번역해주는 명령어
## python manage.py migrate
- models.py에 적힌 내용을 DB에 적용하라는 명령어
## python manage.py createsuperuser
- Admin(관리자)계정 생성

(admin.py에서)
## from .models import Blog
- 같은 폴더 안에 있는 models라는 파일에서 Blog라는 클래스를 가져오라는 명령어
## admin.site.register(Blog)
- admin이라는 사이트에 Blog클래스를 등록

(views.py에서)
## blogs = Blog.objects
- Blog 클래스의 객체들(데이터)을 blogs라는 변수로 처리
## {'blogs':blogs}
- blogs라는 변수를 home.html로 리턴할 때 blogs라는 이름으로 넘김
## {{}}
- view로부터 받아온 데이터를 꺼내서 html화 시킬 때 사용하는 문법
