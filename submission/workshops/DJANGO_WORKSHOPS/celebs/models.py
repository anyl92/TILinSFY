from django.db import models
from faker import Faker

from .validators import validate_too_old, validate_even, validate_too_young
# Bulit-in Validators
from django.core.validators import EmailValidator, MinValueValidator

# Create your models here.
class Celeb(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    @classmethod
    def dummy(cls, n):
        f = Faker()
        for _ in range(n):
            cls.objects.create(first_name=f.first_name(), last_name=f.last_name())


class Person(models.Model):
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100, validators=[EmailValidator('이메일 형식에 맞지 않습니다.')])
    age = models.IntegerField(validators=[MinValueValidator(20, '미성년자 노노')])
    # 함수도 객체기 때문에 () 사용하지 않아도 변수처럼 읽을 수 있다.
