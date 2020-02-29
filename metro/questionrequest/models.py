from django.db import models
from django.db.models import Model
from django.contrib import admin

class Question(models.Model):
    text = models.CharField(max_length=200)

class StationsQuestinon(models.Model):
    station = models.CharField(max_length=200)
    questions = models.ManyToManyField(Question, through='TextElem')
    image = models.ImageField()

class TextElem(models.Model):
    station_name = models.ForeignKey(StationsQuestinon, on_delete=models.CASCADE, verbose_name='Название станции')
    questions_name = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопросы')

class TextElem_inline(admin.TabularInline):
    model = TextElem
    extra = 1

class StationsQuestinonAdmin(admin.ModelAdmin):
    inlines = (TextElem_inline,)
