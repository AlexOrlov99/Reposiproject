from datetime import datetime

from django.db import models
from django.db.models import QuerySet
from django.core.exceptions import ValidationError


from abstracts.models import AbstarctDateTime
from auths.models import CustomUser


class GroupQuerySet(QuerySet):

    HIGH_GPA_LEVEL = 4.0

    def get_students_with_high_gpa(self) -> QuerySet:
        return self.filter(
            group__student__gpa=self.HIGH_GPA_LEVEL
        )


class Group(AbstarctDateTime):
    GROUP_NAME_MAX_LENGTH = 10

    name = models.CharField(
        verbose_name='Имя',
        max_length = GROUP_NAME_MAX_LENGTH
    )
    objects = GroupQuerySet().as_manager()

    def __str__(self) -> str:
        return f'Группа: {self.name}'

    class Meta:
        ordering = (
            'name',
        )
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class StudentQuerySet(QuerySet):
    ADULT_AGE = 18

    def get_adult_student(self) -> QuerySet:
        return self.filter(
            age__gte=self.ADULT_AGE
        )


class Student(AbstarctDateTime):
    MAX_AGE = 27

    user = models.OneToOneField(
        CustomUser,
        verbose_name='пользователь',
        on_delete=models.PROTECT
    )
    age = models.IntegerField(
        'Возраст студента', 
    )
    gpa = models.FloatField(
        'Средний бал'
    )
    group = models.ForeignKey(
        Group, 
        verbose_name='группа',
        on_delete=models.PROTECT
    )
    objects = StudentQuerySet().as_manager()


    def __str__(self) -> str:
        return 'Студент: {0} / {1} / {2}'.format(
            self.user.email,
            self.age,
            self.gpa,
        )

    def save(self,
        *args: tuple,
        **kwargs: dict
        ) -> None:
        if self.age > self.MAX_AGE:
            self.age = self.MAX_AGE
            raise ValidationError(
                f'Допустимый возраст : {self.MAX_AGE}'
            )
        super().save(*args, **kwargs)
    
    def delete(self) -> None:
        datetime_now: datetime = datetime_now()

        self.save(
            update_fields=['datetmie_deleted']
        )
        # super().delete()


    class Meta:
        ordering = (
            'gpa',
        )
        verbose_name = 'Студент'
        verbose_name_plural = 'Стундеты'


class Professor(AbstarctDateTime):
    FULL_NAME_MAX_LENGTH = 20

    TOPIC_JAVA = 'java'
    TOPIC_PYTHON= 'python'
    TOPIC_TYPECSCRIPT = 'typescript'
    TOPIC_RUBY = 'ruby'
    TOPIC_GOLANG = 'golang'
    TOPIC_SQL= 'sql'
    TOPIC_SWIFT = 'swift'
    TOPIC_PHP = 'php'
    TOPIC_DELPHI = 'delphi'
    TOPIC_PERL = 'perl'

    TOPIC_CHOICES = (
        (TOPIC_JAVA, 'Java'),
        (TOPIC_PYTHON, 'Python'),
        (TOPIC_TYPECSCRIPT, 'TypeScrips'),
        (TOPIC_RUBY,'Ruby'),
        (TOPIC_GOLANG, 'Golanfg'),
        (TOPIC_SQL, 'SQL'),
        (TOPIC_SWIFT, 'Swift'),
        (TOPIC_PHP, 'PHP'),
        (TOPIC_DELPHI, 'Delphi'),
        (TOPIC_PERL, 'Perl')
    )

    full_name = models.CharField(
        verbose_name='Полное имя',
        max_length=FULL_NAME_MAX_LENGTH
    )
    topic = models.CharField(
        max_length = FULL_NAME_MAX_LENGTH,
        verbose_name='Предмет',
        choices = TOPIC_CHOICES,
        default = TOPIC_JAVA
    )
    students = models.ManyToManyField(
        Student
    )
    def __str__(self) -> str:
        return f'Профессор: {self.full_name}, Топик: {self.topic}'
    
    def save(self,
        *args: tuple,
        **kwargs: dict
        ) -> None:
        if self.full_name.__len__() > self.FULL_NAME_MAX_LENGTH:
            self.full_name= self.FULL_NAME_MAX_LENGTH
            raise ValidationError(
                f'Допустимый размер строки : {self.FULL_NAME_MAX_LENGTH}'
            )
        super().save(*args, **kwargs)
    
    class Meta:
        ordering = (
            'topic',
        )
        verbose_name = 'Проффессор'
        verbose_name_plural = 'Проффессора'


class HomeworkQueryset(QuerySet):

    def get_not_deleted(self) -> QuerySet:
        return self.filter(datetime_deleted__isnull=True)


class Homework(AbstarctDateTime):

    IMAGE_TYPES =(
        'png',
        'jpg',
        'jpeg'
    )

    user = models.ForeignKey(
        CustomUser,
        verbose_name='загрузчик',
        on_delete=models.PROTECT
    )
    title = models.CharField(
        max_length=100,
        verbose_name='Заголовок',
        )
    subject = models.CharField(
        max_length=100,
        verbose_name='Топик',
        )
    logo = models.ImageField(
        upload_to='homeworks/logos/%Y%m%d',
        verbose_name='Лого',
        max_length=255
        )

    objects = HomeworkQueryset().as_manager()

    @property
    def is_checked(self) -> bool:
        return all(
            self.files.values_list(
                'is_checked', flat=True
            )
        )

    class Meta:
        ordering = (
            'datetime_created',
        )
        verbose_name = 'Домашнее задание'
        verbose_name_plural = 'Домашние задания'


class FileQueryset(QuerySet):

    def get_not_deleted(self) -> QuerySet:
        return self.filter(datetime_deleted__isnull=True)


class File(AbstarctDateTime):

    FILE_TYPES =(
        'txt',
        'pdf'
    )
    title = models.CharField(
        max_length=100,
        verbose_name='Заголовок',
        )
    obj = models.FileField(
        upload_to='homeworks/files/%Y%m%d',
        verbose_name='Файл',
    )
    homework = models.ForeignKey(
        Homework, 
        verbose_name='Домашняя работа',
        on_delete=models.PROTECT,
        related_name = 'files',
    )
    is_checked = models.BooleanField(
        verbose_name='Проверен',
        default = False,
    )
    objects = FileQueryset().as_manager()

    def __str__(self) -> str:
        return f'{self.homework.title} | {self.title}'

    class Meta:
        ordering =(
            '-datetime_created',
        )
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
