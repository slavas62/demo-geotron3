# -*- coding: utf-8 -*-

from django.db import models

class Project(models.Model):
    title = models.CharField(u'Заголовок', max_length=20)
    description = models.CharField(u'Описание', max_length=50)
    image = models.ImageField(u'Изображение')
    url = models.URLField(u'Ссылка')
    position = models.PositiveSmallIntegerField(u'Порядок отображения', default=0)
    visible = models.BooleanField(u'Показать', default = True)
    
    class Meta:
        verbose_name = u'Проект'
        verbose_name_plural = u'Проекты'
