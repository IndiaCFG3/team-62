from django.contrib import admin
from .models import Question,Response,Course

# Register your models here.
admin.site.register(Question)
admin.site.register(Response)
admin.site.register(Course)