from django.db import models


NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class Student(models.Model):
    objects = models.Manager()

    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    avatar = models.ImageField(upload_to='students/', verbose_name='Аватар', **NULLABLE)

    email = models.CharField(max_length=150, verbose_name='Email', unique=True, **NULLABLE)

    is_active = models.BooleanField(default=True, verbose_name='Учится')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'
        ordering = ('last_name',)


class Subject(models.Model):
    objects = models.Manager()

    title = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Студент')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'предмет'
        verbose_name_plural = 'предметы'
