from django.contrib import admin
from .models import Job

# Register your models here.
# регистрация моделей(таблиц) для того тчобы они отображались на панели администратора
admin.site.register(Job)
