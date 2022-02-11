from django.db import models

class AbstarctDateTime(models.Model):

    datatime_created = models.DateTimeField(
        verbose_name='время создания',
        auto_now_add = True
    )
    datatime_updated = models.DateTimeField(
        verbose_name='время обновления',
        auto_now_add = True
    )
    datatime_deleted = models.DateTimeField(
        verbose_name='время удаления',
        null = True,
        blank = True
    )

    class Meta:
        abstract = True

