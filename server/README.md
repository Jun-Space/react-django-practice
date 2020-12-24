## 환경 설정
(프론트에서 맞춰서 작업하려면 가상환경 설정도 해야하는지 잘 모르겠네요)
사용한 프레임워크 (python 버전 3 필요)
python django
python django-rest-freamwork

-실행순서-
1. manage.py가 있는 루트 폴더로 커맨드 접속
2. pip install django // pip install djangorestframework
3. python manage.py makemigrations
4. python manage.py migrate
5. python manage.py createsuperuser  -> admin 계정 생성
6. python manage.py runserver
7. http://127.0.0.1:8000/admin 접속
8. 생성한 슈퍼유저 계정으로 접속
9. ACCOUNT의 Dummy users에 add하여 mock data 생성 가능



## URI
형식 사항에 맞게 수정했습니다.
django에서만 그런지 모르겠는데 조회시 성공이나 이런 메세지를 따로 바디에 넣지는 않고
보통 헤더에 status 정보로 알리는 것 같고 그에 맞는 코드 규약도 맞춰서 세우는게 좋은 것 같아요. 
https://www.django-rest-framework.org/api-guide/status-codes/


