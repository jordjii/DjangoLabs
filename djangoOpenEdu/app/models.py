"""
Definition of models.
"""


from django.db import models
from datetime import datetime
from django.contrib import admin
from django.urls import reverse

class Blog(models.Model):
    title = models.CharField(max_length=100, )


class Blog(models.Model):
    title = models.CharField(max_length = 100, unique_for_date = "posted", verbose_name = "Заголовок")     
    description = models.TextField(verbose_name = "Краткое содержание")    
    content = models.TextField(verbose_name = "Полное содержание")
    posted = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Опубликована")
    image = models.FileField(default = 'temp.jpg', verbose_name = "Путь к картинке")
    
    # Методы класса:

    def get_absolute_url(self):
        return reverse("blogpost", args=[str(self.id)])

    def __str__(self): # метод возврацает название, используемое для представления отдельных записей в административном разделе
        return self.title
    
    # Метаданные - вложенный класс, который задает дополнительные параметры модели:
    class Meta:
        db_table = "Posts" # иня таблицы для модели
        ordering = ["-posted"] # в порядок сортировки данных в модели ("-" означает по убыванию) verbose_name = "статья блога"
        verbose_name = "статья блога" 
        verbose_name_plural = "статья блога" 
        
admin.site.register(Blog)
    
    