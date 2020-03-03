from django.contrib import admin
from .models import *

admin.site.register(Question, StationsQuestinonAdmin)
admin.site.register(StationsQuestinon, StationsQuestinonAdmin)
admin.site.register(Answer)
