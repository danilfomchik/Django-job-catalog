from django.db import models

# Create your models here.

# создание моделей(таблиц)


class Job(models.Model):
    position = models.CharField('Position', max_length=50)
    description = models.TextField('Description')

    def __str__(self):
        return self.position

    class Meta:
        verbose_name = 'Jobs vacancy'
        verbose_name_plural = 'Jobs vacancies'
