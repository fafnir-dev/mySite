from django.db import models
import uuid


class Person(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    name = models.CharField(verbose_name="Имя", max_length=50)
    surname = models.CharField(verbose_name="Отчество", max_length=50)
    lastName = models.CharField(verbose_name="Фамилия", max_length=50)
    nickName = models.CharField(verbose_name="Ник нейм", max_length=50, unique=True)
    email = models.EmailField(verbose_name="Электронная почта", max_length=255, unique=True)
    phone = models.IntegerField(verbose_name="Сотовый телефон", unique=True)
    password = models.CharField(verbose_name="Пароль", max_length=255)


