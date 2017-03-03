from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.db import models

class UserManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Email непременно должен быть указан')

        user = self.model(
            email=UserManager.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



class ExtUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        'Электронная почта',
        max_length=255,
        unique=True,
        db_index=True
    )
    firstname = models.CharField(
        'Фамилия',
        max_length=40,
        null=True,
        blank=True
    )
    lastname = models.CharField(
        'Имя',
        max_length=40,
        null=True,
        blank=True
    )
    register_date = models.DateField(
        'Дата регистрации',
        auto_now_add=True
    )
    
    myURL = models.CharField(
        'URL',
        max_length=10,
        null=True,
        blank=True
    )
    name_comp = models.CharField(
        'Наименование компании',
        max_length=50,
        blank=True
    )
    phone = models.CharField(
        'Телефон',
        max_length=30,
        blank=True
    )
    day_licenz = models.IntegerField(
        'Дней до конца лицензии',
        default=0
    )
    
    is_active = models.BooleanField(
        'Активен',
        default=True
    )
    is_admin = models.BooleanField(
        'Вход в админку',
        default=False
    )
    is_superuser = models.BooleanField(
        'Суперпользователь',
        default=False
    )

    # Этот метод обязательно должен быть определён
    def get_full_name(self):
        return self.email

    # Требуется для админки
    @property
    def is_staff(self):
        return self.is_admin

    def is_superuser(self):
        return self.is_superuser

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
