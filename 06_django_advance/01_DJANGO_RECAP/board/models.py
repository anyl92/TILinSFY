from django.db import models
from django.urls import reverse

class Article(models.Model):
    # id 안넣는 이유, 무조건 생성되게 되어있어서
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 아래는 모두 ORM 에게 확인을 요청하는 과정
    # python manage.py makemigrations board
    # migrations 에서 확인
    # python manage.py sqlmigrate board 0001  > sql 에서 어떤건지 확인
    # python manage.py migrate board 라고 치면 db 에서 생성 및 확인 가능

    # python manage.py shell_plus
    # article = Article()
    # article.title = '안녕'
    # article.content = '안녕안녕'
    # article.save()   == INSERT INTO
    # save가 가능한 이유는 model에 내장되어 있기 때문
    # SELECT * FROM Article == Article.objects.all()
    # SELECT * FROM board.article WHERE id=1
    # == Article.objects.get(id=1)

    # python manage.py shell_plus --print-sql
    # python 코드를 sql 로 번역

    # DELETE FROM board_article WHERE id=1
    # == article = Article.objects.get(id=1) 변수 잡아놓고 삭제
    # article.delete()

    # Article.objects.create(title='hi', content='hihi')
    # 생성

    # python manage.py dbshell > sql 직접 접근

    # article = Article.objects.get(id=2)

    def get_absolute_url(self):  # detail page 가 있을 때
        return reverse("board:article_detail", kwargs={"article_id": self.id})
    

class Comment(models.Model):
    content = models.CharField(max_length=200)  # 검증이 아님, 맥스 넘으면 그냥 잘라버림
    article = models.ForeignKey(Article, on_delete=models.CASCADE)