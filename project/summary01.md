# Basic    
1. startproject   
$ django-admin startproject practice // 새로운 프로젝트 생성   
2. startapp   
 $ python manage.py startapp firstapp // 프로젝트 내 새로운 앱 생성
3. 폴더구조   
practice  
-firstapp   
model.py   
tests.py    
view.py   
urls.py //나중에 생성한 앱 내 urls.py    
    -practice   
    __init__.py   
    settings.py      
    urls.py //프로젝트 내 urls.py   
    wsgi.py      

4. fisrtapp내 app이 있다는 것을 프로젝트에 알리기   
>    INSTALLED_APPS = [   
      'firstapp',// 필수로 추가시키기!!   
      'django.contrib.admin',   
      'django.contrib.auth',   
      'django.contrib.contenttypes',   
      'django.contrib.sessions',      
      'django.contrib.messages',   
      'django.contrib.staticfiles',   
 ]   
 5. 순서-시스템   
 1) Django는 프로젝트 urls.py를 본다.   
 2) 해당하는 url을 찾는다.   
 3) 그에 해당하는 view가 있으면 그 view를 보여준다.   

 6. 순서-개발자   
    1) view만들기   
    2) view와 url 연결하기   
    3) url mapping : 프로젝트내 app은 여러개를 생성할 수 있으므로 프로젝트 urls.py역할을 app내 urls.py로 옮기기-> include함수 이용    
    $ cp urls.py ../firstapp   
    4) 변수화 : 일일이 url시켜주는 것 대신 사용 <int:nuber>
    5) template namesapcing ex) firstapp/templates/firstapp/index.html
    6) html파일 만든것을 view에게 알리기
    7) 시간 설정 : settings.py 수정
    8)

 7) Live Local Server 실행   
 $ python manage.py runserver 

 8) anchor tag url 설정(=html의 anchor태그안에 url넣는법)   
    변수 : {{}} - 변수를 다룬다.   
    태그 : {% %} - 로직을 다룬다.   
    필터 : {{value|length}} - 변수에 필터 적용   

9) static file   
    1) settings.py 값 수정   
    2) template 파일에  {% load static%} 코드 추가 

10) Http Request & Response Flow   
우리가 브라우저의 주소창에 어떤 웹페이지의 주소를 입력한다면 다음의 일련의 과정이 일어난다.   
    1. Client가 특정주소로 request를 보낸다.
    2. django 웹 앱 request가 들어온다.
    3. url conf 모듈을 이용하여 request의 url을 확인한다.
    4. 해당 url에 대한 처리를 담당하는 view를 결정한다.
    5. view는 Logic을 실행한다.
    6. 필요한 경우, Model을 통해 데이터를 처리한다.
    7. Template를 기반으로 최종 html 코드를 생성한다.
    8. 생성된 html 코드를  client로 보낸다.
    9. client가 받은 html 코드를 랜더링한다. 

11) MTV pattern   
    M(model) : 모델 클래스, 데이터 객체 정의와 그 데이터 (models.py)   
    T(template) : 사용자에게 보여지는 인터페이스 화면 (templates/*.html)   
    V(view) : 데이터를 가져오고 적절하게 가공하여 그 결과를 템플릿에게 전달하는 역할(views.py)

# Model
1) 순서-개발자   
    1. model.py 정의   
    2. migrations : migrate 할 준비 (=git의add)  
    $ python manage.py makemigrations second   
    3. migrate : 실제 DB로 모델 클래스가 DB에 맞게 번역되어 DB에 들어감 (=git의 commit)   
    $ python manage.py migrate second
    4. Datebase에 date 저장하기(로컬)   
    $ python manage.py shell
    >  from second.models import Post   
    post = Post.objects.create(title='this is title', content='this is content')   
    post.save()   
    posts = Post.objects.all()
    posts   
    <QuerySet [<Post: Post object (1)>, <Post: Post object (2)>, <Post: Post object (3)>, <Post: Post object (4)>, <Post: Post object (5)>, <Post: Post object (6)>, <Post: Post object (7)>]>
    >
    5. 사용자가 입력 form.py 만들기   
    6. form을 사용하도록 view 로직 구현
    7. html 생성   
    8. urls.py 로 연결   
    9. views.py에서 confirm 코드 추가(타당성체크)
    10. template에 confirm.html 추가
    11. urls.py에서 confirm url mapping 하기
    12. 비워둔 form action값에 confirm 추가   
    
2) 사용자가 입력할 Form   
```
<form action=”데이터가 전달될 주소(요청/이동할 주소)” method=”http 요청 방식(GET/POST/PUT/DELETE">
  <input type=”text” name=”title”/>
  <button type=”submit”>입력</button>
</form>
```

3. Model Form = 기존의 form형태가 아닌 model.py에서 정의해준 model을 가져다 쓰는것 




   