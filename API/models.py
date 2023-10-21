from django.db import models

from django.contrib.auth.models import AbstractUser




class LearningPlace(models.Model): # Учебное заведение 
    name = models.CharField(max_length=150)
    users_classes = models.ManyToManyField('LearningPlaceClasses',blank=True)
    users = models.ManyToManyField('User',blank=True)
    def __str__(self) -> str:
        return f'{self.name}'
    class Meta:
        verbose_name = 'Учебное заведение'
        verbose_name_plural = 'Учебные заведения'

class BaseLearningPlace(models.Model):
    learning_place = models.ForeignKey(LearningPlace,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100,blank=True)
    students_class = models.ForeignKey('LearningPlaceClasses',on_delete=models.CASCADE,null=True)
    class Meta:
        abstract = True    

class LearningPlaceTimetableLesson(BaseLearningPlace): # Уроки
    serial_number = models.SmallAutoField(primary_key=True)
    teacher = models.ForeignKey('User',on_delete=models.CASCADE,null=True)
    start = models.TimeField(null=True)
    end = models.TimeField(null=True)
    def __str__(self) -> str:
        return f'{self.learning_place}/{self.serial_number}/{self.students_class}'
    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
class LearningPlacetTimetable(BaseLearningPlace): # Расписание
    data = models.DateField(auto_now=True)
    lessons = models.ManyToManyField(LearningPlaceTimetableLesson,blank=True)
    def __str__(self) -> str:
        if self.name:
            return f'{self.learning_place}/{self.name}/{self.students_class}'
        return f'{self.learning_place}/{self.data}/{self.students_class}'
    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'

class LearningPlaceClassUser(BaseLearningPlace): # Класс пользователя 
    def __str__(self) -> str:
        return f'{self.learning_place}/{self.name}'
    class Meta:
        verbose_name = 'Тип пользователя'
        verbose_name_plural = 'Типы пользователей'

class LearningPlaceClasses(models.Model): # Учебный класс пользователя
    name = models.CharField(max_length=50)
    users = models.ManyToManyField('User',blank=True)
    learning_place = models.ForeignKey('LearningPlace',on_delete=models.CASCADE,null=True)
    timetable = models.ManyToManyField(LearningPlaceTimetableLesson,blank=True)
    def __str__(self) -> str:
        return f'{self.name}'
    class Meta:
        verbose_name = 'Учебное заведение'
        verbose_name_plural = 'Учебные заведения'

class User(AbstractUser): # Пользователь
    TYPE_USER = [
        ("TEA","Учитель"),
        ("STU","Ученик"),
        ("ADM","Администратор")
    ]
    type_user = models.CharField(
        max_length=3,
        choices=TYPE_USER,
        default="STU",
    )
    learning_place = models.ForeignKey(LearningPlace,on_delete=models.CASCADE,null=True,blank=True)
    user_class = models.ForeignKey(LearningPlaceClasses,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self) -> str:
        return f'{self.type_user}_{self.username}'
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'