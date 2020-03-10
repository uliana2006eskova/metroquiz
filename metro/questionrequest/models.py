from django.db import models
from django.db.models import Model
from django.contrib import admin
from django_summernote.fields import SummernoteTextField
from django.contrib.auth.models import User
class Question(models.Model):
    class Meta:
        verbose_name='Вопрос'
    station = models.CharField(max_length=200, verbose_name="Название станции")
    text = SummernoteTextField(verbose_name="Текст вопроса")
    who = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Для кого вопросы")

class Answer(models.Model):
    class Meta:
        verbose_name = "Ответ"
    text = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор ответа", blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Вопрос", blank=True)


class Information(models.Model):
    class Meta:
        verbose_name='Информация'
    station = models.CharField(max_length=200, verbose_name="Название станции")
    text = SummernoteTextField(verbose_name="Информация")
    who = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Для кого вопросы")