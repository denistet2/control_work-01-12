from django.contrib import admin




# Register your models here.
from .models import Person
#admin.site.register(Person)

class PersonAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = (('name', 'department', 'salary', 'job_title'))
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('department',)
    # Добавляем возможность фильтрации по дате
    list_filter = ('salary',)

# При регистрации модели Post источником конфигурации для неё назначаем
# класс PersonAdmin
admin.site.register(Person, PersonAdmin)

from .models import Department
admin.site.register(Department)




